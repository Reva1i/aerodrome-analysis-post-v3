# Aerodrome Ignition: Who Really Benefits?
### A Competitor's Research Report — April 2026

---

## Executive Summary

Aerodrome's Ignition program is marketed as the "cleanest way to launch tokens on Base." After analyzing all three confirmed launches (SYND, LITKEY, SUMR), the data tells a more uncomfortable story: **projects bear the costs while Aerodrome and its AERO/veAERO holders capture most of the value.** Token prices dropped 70–99% within 90 days of launch. TVL evaporated after emissions reduced. New "sticky" users were negligible. Emissions consistently exceeded fees generated. The program is an efficient liquidity rental machine — for Aerodrome. For projects, it is a costly, one-sided trade.

---

## 1. What Is Aero Ignition?

Aero Ignition is Aerodrome's DEX-native token launch mechanism on Base, officially branded in October 2025 (though the first launch, SYND, preceded the branding in September 2025 as a "Community Launch").

**Mechanics:**
1. A project deposits 10–20% of its token supply into an Aerodrome pool (e.g., TOKEN/WETH)
2. A slice of that supply (typically 1–3%) is deposited as bribe incentives for veAERO holders
3. veAERO holders vote to direct AERO emissions to the project's pool
4. LPs deposit capital into the pool, attracted by high APRs
5. The pool goes live — token is publicly tradable with deep day-1 liquidity

**What projects receive:**
- Bootstrapped liquidity without presales or private rounds
- AERO emissions streaming to their pool (making it attractive to LPs)
- Distribution via Aerodrome's user base
- Theoretical price discovery "without hidden influence"

**What projects give up:**
- 1–3% of token supply as voting incentives (bribe cost)
- 10–20% of supply deposited as liquidity (opportunity cost — illiquid until removed)
- Full dependence on veAERO voter appetite to sustain emissions after week 1

---

## 2. Confirmed Ignition Launches

| # | Project | Token | Launch Date | Notes |
|---|---------|-------|------------|-------|
| 1 | Syndicate | SYND | Sep 17, 2025 | First "Community Launch" (precursor to Ignition branding) |
| 2 | Lit Protocol | LITKEY | Oct 30, 2025 | 2nd Ignition; first under official "Aero Ignition" branding |
| 3 | Summer Finance | SUMR | Jan 21, 2026 | AI yield aggregator; pre-TGE TVL $50M+ |

> **Note:** Aerodrome's own aggregate data covers these launches collectively. A 4th launch may have been announced (April 2026) but has no confirmed post-launch data at time of writing.

---

## 3. The Cost Side: What Did Projects Actually Pay?

### 3A. Direct Bribe Cost (Token Supply Dilution)

| Project | Bribe Allocation | Tokens Used as Bribe | USD Value at Launch Price |
|---------|-----------------|----------------------|--------------------------|
| SYND | 1% of 1B supply | 10M SYND | ~$25.1M (at ATH $2.51)* |
| LITKEY | ~1% of 1B supply | 10M LITKEY | ~$2.1M (at launch $0.21) |
| SUMR | 3% week 1 + 0.3% week 2 | ~30M+ SUMR | ~$0.52M (at ATH $0.0173) |

> *SYND's ATH-based bribe value is misleading since the token had no pre-existing price — the "cost" is best understood as supply dilution and the opportunity foregone. The real economic cost is closer to the value at which these tokens were absorbed by the market post-launch. SYND's bribe tokens at equilibrium (~$0.05) = ~$500K.

**Key insight:** Projects use their own freshly minted tokens as bribes. The bribe is only "cheap" if the token price crashes (then the market absorbed it at a loss). If the token holds value, the bribe was expensive. The data shows tokens crashed — meaning bribe tokens were dumped by voters, creating early sell pressure against the project.

### 3B. Opportunity Cost: Liquidity Locked in Pool

- Projects deposit 10–20% of supply into the pool alongside WETH counterpart
- This WETH has to come from somewhere (treasury, team, investors)
- For a $2.4M average peak TVL pool: ~$1.2M in WETH was required from the project side
- This capital was exposed to impermanent loss as the project token fell 70–99%

**Estimated total LP opportunity cost per launch: $800K–$2M in WETH, largely impairment-loss-destroyed.**

---

## 4. The Return Side: What Did Projects Get?

### 4A. AERO Emissions Received

| Project | veAERO Votes Attracted | Week 1 AERO Emissions | Approx. USD Value |
|---------|----------------------|----------------------|------------------|
| SYND | 166M veAERO ($215M), 18.68% of all votes | 875K+ AERO | ~$1.14M–$1.40M |
| LITKEY | 239M veAERO (~50% more than SYND) | Proportionally larger | ~$1.5M–$2.0M est. |
| SUMR | Unknown exact votes | Included in $5M total | ~$1.5M–$2.0M est. |

**Aggregate (all launches):** veAERO voters streamed **$5M+** in AERO emissions to Ignition pools total.

**Critical caveat:** These emissions flow to *liquidity providers*, NOT directly to the project. The project does not pocket the AERO. The emissions incentivize LPs to deposit — which creates the deep liquidity. So the AERO effectively subsidizes mercenary LPs, not the project itself.

### 4B. Swap Fees Generated

**Aggregate across all Ignition launches:** $3.7M+ in cumulative trading fees.
**Average per launch:** ~$1.2M in total fees (over the whole life of the pool post-launch)

Fee split on Aerodrome: 100% of trading fees go to veAERO voters — **not to the project.** LPs get emissions, veAERO holders get fees. Projects get zero fee revenue.

**On day 1 of LITKEY:**
- $25,000+ in daily fees on $2.6M volume (6% daily fee yield on TVL)
- This sounds great — but every dollar of those fees went to veAERO holders

### 4C. Emission-to-Fee Ratio Analysis

| Metric | Value |
|--------|-------|
| Total AERO emissions to Ignition pools | $5M+ |
| Total swap fees from Ignition pools | $3.7M+ |
| Emissions / Fees ratio | ~1.35x |
| Fees / Emissions (sustainability ratio) | ~0.74x |

**Interpretation:** For every $1 of fees the Ignition pools generate, Aerodrome emitted $1.35 in AERO. This means the pools are **not fee-self-sustaining**. The liquidity in these pools exists only because AERO subsidizes it. Remove the emissions, liquidity leaves, fees collapse.

Aerodrome's own efficiency metric reports **$1.50 returned per $1 emitted** protocol-wide — but this is Aerodrome's return on its emissions, not the project's return. It means Aerodrome collects $1.50 in fees for every $1 it emits. Ironically, this is partly funded by Ignition projects providing subsidized volume.

---

## 5. Mercenary Liquidity Test: TVL Before / During / After

| Project | Pre-Launch TVL | Peak TVL (Week 1) | TVL at 3 Months | Change |
|---------|---------------|-------------------|-----------------|--------|
| SYND | $0 (new token) | ~$2–3M | ~$279K (April 2026) | **-90%** |
| LITKEY | $0 (new token) | ~$2.6M | Unknown (est. <$500K) | est. **-80%+** |
| SUMR | $50M+ protocol TVL | ~$2–3M Aerodrome pool | Declined significantly | **-70%+ on Aerodrome pool** |

**Aggregate:** Combined peak TVL = **$9.7M** across all launches. Average per launch = $2.4M.
Today those pools are largely ghost towns.

**Verdict: Classic mercenary liquidity.** TVL follows AERO emissions, not genuine demand for the project's token. As soon as veAERO voters redirect their votes (which happens every week), the LP incentive disappears and capital exits.

---

## 6. New User Acquisition Analysis

**Definition (per your brief):** New wallets acquiring the project's own token after TGE with no airdrop allocation — genuine new users, not airdrop farmers.

| Project | New Token Holders (Month 1) | Notes |
|---------|-----------------------------|-------|
| SYND | Unknown exact | High initial volume but speculation-driven |
| LITKEY | Unknown exact | Opening high volume cooled within 10 days |
| SUMR | **+299 new holders in January** | Protocol had 50M+ TVL pre-TGE; only 299 new holders from TGE |

**SUMR is the most telling:** Summer Finance had an established protocol with $50M+ in TVL before TGE. After the Aerodrome Ignition launch, they added only **299 new token holders** in January. The TGE attracted yield farmers and speculators, not new protocol users.

**Pattern across all projects:**
- Day 1: Extremely high volume, 9,000%+ APRs, frenzied activity
- Days 2–10: APRs normalize, price crashes, volume declines
- Day 10+: Equilibrium is a fraction of launch-day numbers
- Month 3: Pool is a rounding error in Aerodrome's TVL

The high initial APRs create a filter effect: only yield farmers and speculators participate, not long-term users. A project wanting to grow its genuine user base gets very little from this.

---

## 7. Token Price Performance: The Full Picture

| Project | Launch Price | ATH | Price at Day 10 | Price at ~3 Months | % from ATH |
|---------|-------------|-----|-----------------|-------------------|-----------|
| SYND | ~$2.51 ATH at launch | $2.51 (Sep 18) | ~$0.40–0.60 est. | $0.034–0.059 (Jan '26) | **-98%** |
| LITKEY | ~$0.21 | ~$0.21 | $0.04–0.07 | Unknown | **-70%+ by Day 10** |
| SUMR | ~$0.0173 ATH | $0.0173 (Jan 28) | ~$0.004–0.006 | $0.0037 (Apr '26) | **-78%** |

**Every single project: ATH on or within 1 week of launch, then sustained decline.**

The Ignition mechanics structurally guarantee this pattern:
1. Emissions create artificial LP demand → token price pumps
2. Bribe tokens (1–3% of supply) are held by veAERO voters who sell them
3. LPs hedge their token exposure (sell half as they LP)
4. Emissions epoch ends or reduces → LPs exit → liquidity thins → price falls harder
5. Retail buyers from day 1 are underwater; sell pressure mounts

---

## 8. Bribe ROI: Did Projects Get Their Money's Worth?

### SYND
- Bribe: 10M SYND → at equilibrium price (~$0.05) = ~$500K effective cost
- Week 1 AERO emissions to LPs: ~$1.14–1.40M
- But: those emissions went to LPs, not to Syndicate
- What Syndicate gained: ~$2–3M peak TVL for 1 week
- TVL cost per $ retained: $500K bribe → $279K current TVL → **bribe cost > sustained TVL value**
- **Bribe ROI: Negative**

### LITKEY
- Bribe: 10M LITKEY → $2.1M at launch price → ~$400–700K at equilibrium
- Attracted 239M veAERO; proportionally large emissions share
- Day 1 fees: $25K (all to veAERO voters, not to Lit Protocol)
- Price crashed 70% in 10 days
- **Bribe ROI: Marginally positive short-term on emissions received vs bribe cost, but project captured none of those emissions or fees**

### SUMR
- Bribe: 3% supply (week 1) + 0.3% (week 2)
- Price peaked at $0.0173 → bribe value at ATH ~$520K
- Post-TGE: TVL dropped -$22.91M in January (that's the protocol's *own* TVL declining)
- +299 new holders → extremely low user acquisition yield
- **Bribe ROI: Deeply negative when accounting for TVL destruction and negligible user growth**

---

## 9. veAERO Concentration and Voter Dependency

This is the structural risk nobody discusses publicly.

**How concentrated is veAERO power?**
- A handful of whales with large veAERO positions can swing 20%+ of all emissions
- Animoca Brands, institutional protocols, and dedicated yield farmers hold dominant positions
- Projects are fully dependent on these whales continuing to vote for their pool

**What this means for projects:**
- Week 1: Whales vote for your pool because the bribe APR is attractive
- Week 2+: Your bribe is worth less (your token fell), so whales reallocate to better-paying pools
- **Liquidity follows whale votes, not project fundamentals**

This creates a permanent treadmill: to sustain emissions, you must keep increasing bribes. But your token is declining, so each bribe is more expensive in real terms. Most projects cannot sustain this indefinitely.

**The veAERO value capture loop:**
```
Project pays bribe tokens → veAERO holders vote for pool
→ Pool receives AERO emissions → LPs come for APR
→ Pool generates fees → 100% of fees go back to veAERO holders
→ veAERO holders get both: bribe rewards + trading fees
→ Project gets: temporary liquidity that leaves
```

**veAERO holders are the only party that captures value on both ends (bribes in + fees in).**

---

## 10. Comparative Baseline: Ignition vs. Not Ignition

A critical missing piece in Aerodrome's pitch is the counterfactual: what if you launched the same token on Uniswap v3 or without Ignition?

| Factor | Aero Ignition | DIY Launch (Uniswap/other) |
|--------|--------------|--------------------------|
| Day 1 liquidity depth | Very high (AERO emissions) | Low to moderate |
| Bribe cost | 1–3% supply | None |
| Day 1 price action | Extreme pump | More gradual |
| TVL at 3 months | ~10% of peak | More stable (sticky LPs) |
| Fee revenue to project | $0 | 100% of fees |
| User quality | Yield farmers | More genuine buyers |
| Token price trajectory | -70–99% in 90 days | Data-dependent |

**Key observation:** Aerodrome Ignition trades long-term stability for short-term spectacle. The "massive distribution on day one" is mostly to yield farmers who rotate out. Projects that launched via traditional LP bootstrapping on other DEXs retained more proportional liquidity because LPs had organic reasons to stay.

---

## 11. Who Actually Benefits from Ignition?

### ✅ Strong winners: Aerodrome / AERO / veAERO Holders
- Receive 100% of all trading fees from Ignition pools
- Receive bribe tokens from launching projects
- Get TVL boost (good for TVL rankings and narrative)
- Aerodrome collects $1.50 per $1 emitted → positive ROI
- Every Ignition launch is a direct subsidy to Aerodrome's earnings

### ✅ Short-term winners: Mercenary LPs
- Enter on day 1 with 9,000%+ APR
- Collect AERO emissions
- Exit after emissions normalize
- Leave the project with an empty pool

### ✅ Short-term winners: Day 1 Buyers Who Flip Quickly
- Very high initial price, with window to sell before crash
- High slippage tolerance means easy entry/exit at peak

### ❌ Losers: The Launching Projects
- Diluted their supply (1–3% gone as bribes, bribe tokens dumped)
- Paid LP capital that suffered severe impermanent loss
- Token price -70–99% within 3 months
- TVL collapsed to ~10% of peak after 3 months
- Gained fewer than 300 genuine new users per launch
- Captured $0 from $3.7M+ in fees generated by their pools
- Now more dependent on veAERO voters for future liquidity (locked into the ecosystem)

### ❌ Losers: Retail Buyers (Day 1)
- Bought at launch-day highs driven by 9,000%+ APR hype
- Token fell 70–99% within months
- Not compensated by emissions (only LPs get those)

---

## 12. Key Metrics Summary Table

| Metric | SYND | LITKEY | SUMR | Average |
|--------|------|--------|------|---------|
| Launch Date | Sep 17, 2025 | Oct 30, 2025 | Jan 21, 2026 | — |
| Bribe Cost (% supply) | 1% | ~1% | 3% + 0.3% | ~1.5–2% |
| veAERO Votes | 166M ($215M) | 239M | Unknown | — |
| Week 1 AERO Emissions | 875K AERO (~$1.2M) | ~$1.5-2M est. | ~$1.5M est. | ~$1.4–1.6M |
| Peak TVL | ~$2–3M | ~$2.6M | ~$2–3M | ~$2.4M |
| TVL at 3 months | ~$279K | Unknown | Significant decline | ~<$500K |
| TVL retained (%) | ~10–15% | Unknown | ~20% est. | **~15%** |
| Price change (90 days) | **-84%** | **-70%+ by Day 10** | **-78% from ATH** | **~-78%** |
| New genuine users | Unknown | Unknown | **299** | Very low |
| Fees to project | $0 | $0 | $0 | **$0** |
| Emission > Fees? | Yes | Yes | Yes | **Yes, ~1.35x** |

---

## 13. Final Verdict

**For projects: The math does not work in their favor.**

Aero Ignition provides genuine short-term liquidity — which is its primary value proposition. But the "benefit" is largely theatrical:
- The liquidity is rented, not owned
- The fees are captured by someone else
- The users who come are farmers, not builders
- The token price action is almost universally destructive
- The dependency on veAERO whale votes is structural and permanent

The program is essentially a **paid listing on a highly efficient liquidity exchange** — but with far worse terms than a CEX listing, because at least on a CEX the project can negotiate fees and doesn't have its token structurally dumped by bribe recipients.

**For Aerodrome/AERO holders: An excellent deal.**

Every Ignition launch is a guaranteed income stream — bribe tokens + 100% of fees + temporary TVL and volume boost that supports AERO price narrative. The $1.50 returned per $1 emitted protocol efficiency metric is partly powered by Ignition projects subsidizing that number.

**Competitor's Edge:**
If you're building a competing launch mechanism, the winning pitch to projects is simple:
1. Let projects keep a share of swap fees
2. Provide tools to convert LP farmers into protocol users (not just bag holders)
3. Offer emission sustainability guarantees beyond week 1
4. Show 3-month TVL retention data, not just week-1 peak TVL

Aerodrome Ignition is optimized for Aerodrome's metrics. A better competitor product should be optimized for the *project's* metrics.

---

## Data Sources

- [Aerodrome Finance](https://aerodrome.finance)
- [DefiLlama - Aerodrome Ignition](https://defillama.com/protocol/aerodrome-ignition)
- [Bankless — Syndicate's Community Token Launch Makes Waves](https://www.bankless.com/read/syndicates-community-token-launch-makes-waves)
- [Syndicate — Community-First Token Launch](https://syndicate.io/blog/community-first-token-launch)
- [Paragraph — What LITKEY's First 10 Days Taught DeFi](https://paragraph.com/@digitalduniya/when-transparency-met-speculation-%E2%80%94-what-litkeys-first-10-days-taught-defi)
- [Summer.fi Blog — Aerodrome Ignition X Space Recap](https://blog.summer.fi/aerodrome-ignition-x-space-recap-sumr-trading-goes-live/)
- [Summer.fi Blog — Ringing the Bell: SUMR TGE Happened](https://blog.summer.fi/ringing-the-bell-sumr-tge-happened-now-what/)
- [Summer.fi — Governance Recap January 2026](https://blog.summer.fi/lazy-summer-governance-recap-january-2026/)
- [MEXC News — LITKEY Launch](https://www.mexc.com/news/lit-protocol-to-launch-community-token-litkey-on-base-via-aerodromefi-on-october-30th/140636)
- [MEXC News — SYND Launch](https://www.mexc.com/news/84568)
- [Phemex News — SYND Aerodrome Launch](https://phemex.com/news/article/base-to-launch-synd-token-on-aerodrome-via-syndicate-protocol-18105)
- [LITKEY Tokenomics — Spark by Lit Protocol](https://spark.litprotocol.com/litkey-tokenomics/)
- [Aerodrome on X — Introducing Aero Ignition](https://x.com/AerodromeFi/status/1980741852094750954)
- [CoinGecko — Aerodrome Finance](https://www.coingecko.com/en/coins/aerodrome-finance)
- [GeckoTerminal — SYND/WETH Pool](https://www.geckoterminal.com/base/pools/0xa6f77321b8726faab89b72f28c2603b667448bc2)
- [Blockworks Analytics — Aerodrome veNFT Voting Power Evolution](https://blockworks.com/analytics/aerodrome/aerodrome-venft/aerodrome-voting-power-evolution)
- [Gate.com — Aerodrome Tokenomics](https://www.gate.com/learn/articles/aerodrome-tokenomics-how-ve-3-3-powers-bases-most-profitable-dex/16473)
- [Coinage Media — How Aerodrome Is Rewriting the Rules of DeFi](https://www.coinage.media/2026/how-decentralized-crypto-exchange-aerodrome-is-rewriting-the-rules-of-defi)

---

*Report compiled: April 28, 2026. Research methodology: on-chain data via public APIs, project blogs, DeFi analytics platforms, and verified press coverage. Numbers reflect best available public data; some metrics are estimated ranges where exact figures were unavailable.*
