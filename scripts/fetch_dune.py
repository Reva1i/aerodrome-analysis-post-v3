"""
Fetch latest Aerodrome migration data from Dune Analytics and write to data/*.json.

Usage:
  DUNE_API_KEY=your_key python scripts/fetch_dune.py

Query IDs (update after creating permanent non-temp queries on Dune):
  EMISSIONS_QUERY_ID  : Q-7360619  (24-gauge per-epoch emissions)
  PROTOCOL_QUERY_ID   : Q-7360620  (protocol totals + AERO price)
  SACRIFICE_QUERY_ID  : Q-7360622  (sacrifice pool ranking)
"""

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

try:
    import requests
except ImportError:
    sys.exit("Missing dependency: pip install requests")

API_KEY = os.environ.get("DUNE_API_KEY", "")
if not API_KEY:
    sys.exit("DUNE_API_KEY environment variable is not set.")

BASE_URL = "https://api.dune.com/api/v1"
HEADERS  = {"X-Dune-API-Key": API_KEY}
DATA_DIR = Path(__file__).parent.parent / "data"

# ── Replace with permanent (non-temp) query IDs after recreating on Dune ──
EMISSIONS_QUERY_ID = 7360619
PROTOCOL_QUERY_ID  = 7360620
SACRIFICE_QUERY_ID = 7360622
# ──────────────────────────────────────────────────────────────────────────

BOOTSTRAP_EPOCH = "2026-04-09"
LAUNCH_EPOCH    = "2026-04-16"


def fetch_results(query_id: int) -> list[dict]:
    url  = f"{BASE_URL}/query/{query_id}/results"
    resp = requests.get(url, headers=HEADERS, timeout=60)
    resp.raise_for_status()
    return resp.json().get("result", {}).get("rows", [])


def build_emissions(rows: list[dict]) -> dict:
    bootstrap: dict[str, float] = {}
    launch_v2: dict[str, float] = {}
    launch_v3: dict[str, float] = {}
    price_boot = price_launch = 0.0

    for r in rows:
        epoch = r.get("epoch_start", "")[:10]
        label = r.get("pool_label", "")
        ver   = r.get("pool_version", "")
        amt   = float(r.get("aero_amount", 0))
        price = float(r.get("aero_price", 0))

        if epoch == BOOTSTRAP_EPOCH:
            price_boot = price or price_boot
            if ver == "V2":
                bootstrap[label] = amt
        elif epoch == LAUNCH_EPOCH:
            price_launch = price or price_launch
            if ver == "V2":
                launch_v2[label] = amt
            elif ver == "V3":
                launch_v3[label] = amt

    all_labels = sorted(
        set(bootstrap) | set(launch_v2) | set(launch_v3),
        key=lambda l: launch_v2.get(l, 0) + launch_v3.get(l, 0),
        reverse=True,
    )
    pairs = [
        {
            "label":        lbl,
            "v2_bootstrap": bootstrap.get(lbl, 0),
            "v2_launch":    launch_v2.get(lbl, 0),
            "v3_launch":    launch_v3.get(lbl, 0),
        }
        for lbl in all_labels
    ]
    return {
        "updated_at":           _today(),
        "bootstrap_epoch":      BOOTSTRAP_EPOCH,
        "launch_epoch":         LAUNCH_EPOCH,
        "aero_price_bootstrap": round(price_boot, 4),
        "aero_price_launch":    round(price_launch, 4),
        "pairs":                pairs,
    }


def build_protocol(rows: list[dict]) -> dict:
    epochs = [
        {
            "epoch_start":   r.get("epoch_start", "")[:10],
            "aero_minted":   float(r.get("aero_minted", 0)),
            "aero_price":    round(float(r.get("aero_price", 0)), 4),
            "active_gauges": int(r.get("active_gauges", 0)),
        }
        for r in sorted(rows, key=lambda x: x.get("epoch_start", ""))
    ]
    return {"updated_at": _today(), "epochs": epochs}


def build_sacrifice(rows: list[dict]) -> dict:
    pools = [
        {
            "rank":       int(r.get("rank", 0)),
            "pool_label": r.get("pool_label", r.get("gauge_address", "unknown")),
            "pre_avg":    round(float(r.get("pre_avg_aero", 0)), 0),
            "post_avg":   round(float(r.get("post_avg_aero", 0)), 0),
            "delta":      round(float(r.get("aero_weekly_delta", 0)), 0),
            "delta_usd":  round(float(r.get("delta_usd", 0)), 0),
            "same_pair":  bool(r.get("same_pair", False)),
        }
        for r in rows
    ]
    validated       = [p for p in pools if p["rank"] != 1]
    total_delta     = round(sum(p["delta"]     for p in validated), 0)
    total_delta_usd = round(sum(p["delta_usd"] for p in validated), 0)
    return {
        "updated_at":                _today(),
        "total_validated_delta":     total_delta,
        "total_validated_delta_usd": total_delta_usd,
        "note": "Rank 1 excluded: only 1 pre-migration epoch, baseline unreliable.",
        "pools": validated,
    }


def _today() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def _write(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"  wrote {path.name}")


def main() -> None:
    print("Fetching Dune data...")
    _write(DATA_DIR / "emissions.json", build_emissions(fetch_results(EMISSIONS_QUERY_ID)))
    _write(DATA_DIR / "protocol.json",  build_protocol(fetch_results(PROTOCOL_QUERY_ID)))
    _write(DATA_DIR / "sacrifice.json", build_sacrifice(fetch_results(SACRIFICE_QUERY_ID)))
    print("Done.")


if __name__ == "__main__":
    main()
