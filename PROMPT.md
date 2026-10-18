# PROMPT.md — EMA Hourly Continuation Research

You are the autonomous quantitative-research and software-engineering agent for this repository (**Quantitative-Research-Prompt-EMA-hourly-continuation-**). Your mission is to design, implement, backtest, and rigorously evaluate an **EMA hourly continuation** strategy on cryptocurrency markets, producing reproducible, net-of-cost evidence—not optimistic charts.

---

## 1. Strategy specification (authoritative)

### 1.1 Timeframe and indicators
- Bar frequency: **1-hour** (exchange or aggregated hourly OHLCV; document the source and timezone).
- Indicators on each symbol's hourly close series:
  - `EMA50` = exponential moving average of close, period 50
  - `EMA100` = exponential moving average of close, period 100
- Warm-up: no signals until both EMAs are fully defined (at least 100 closed hourly bars of valid data).

### 1.2 Trend filter
- **Bullish regime:** `EMA50 > EMA100` (on the bar used for the decision).
- **Bearish regime:** `EMA50 < EMA100`.
- Equal EMAs: no new entries.

### 1.3 Entry rules (continuation)
Use **confirmed closed-bar** logic only (no intra-bar lookahead).

**Long entry** (all must hold on the signal bar `t`):
1. Bullish regime: `EMA50[t] > EMA100[t]`
2. Price cross above EMA50: `close[t-1] <= EMA50[t-1]` **and** `close[t] > EMA50[t]`
3. Prefer evaluating crosses with the **same bar's** EMA values used consistently; document the exact implementation.

**Short entry** (mirror):
1. Bearish regime: `EMA50[t] < EMA100[t]`
2. Price cross below EMA50: `close[t-1] >= EMA50[t-1]` **and** `close[t] < EMA50[t]`

### 1.4 Stop loss and take profit (1:1 risk–reward)
Interpret the user's rule as follows (document this interpretation in code and results):

- **Risk distance** at entry: absolute distance from entry price to the **EMA100** level on the signal bar  
  `risk = abs(entry_price - EMA100[t])`
- If `risk` is zero or pathologically small (e.g. entry almost on EMA100), **skip the trade** (do not invent a minimum risk).
- **Stop loss:**  
  - Long: `entry_price - risk` (conceptually at the EMA100 distance below entry; equivalent to SL at `EMA100` when entry is above EMA100)  
  - Short: `entry_price + risk`
- **Take profit (1:1):**  
  - Long: `entry_price + risk`  
  - Short: `entry_price - risk`

Optional clarity for implementation:
- For a long with `entry > EMA100`, SL at `EMA100` and TP at `entry + (entry - EMA100)` is identical to the risk formula above.
- Always store entry, SL, TP, risk%, and EMA values on the trade record.

### 1.5 Position and lifecycle
- Default: **one position per symbol** at a time (no pyramiding unless a later experiment explicitly tests it).
- Entry fill assumption (document and keep fixed for the baseline): next-bar open after signal, or signal-bar close—**pick one, state it, and do not mix**.
- Exit: first touch of SL or TP on subsequent bars (use high/low for stop/target hits; define OHLC path order if both could hit in the same bar—e.g. conservative: adverse first).
- No time stop in the baseline; a max-hold bars rule may be added later as a controlled mutation.
- No re-entry on the same bar as exit unless explicitly tested later.

### 1.6 Sizing and costs (baseline)
- Fixed fractional risk **or** fixed notional per trade; state the choice. Prefer risk-based sizing: risk a fixed fraction of equity per trade when equity curve is simulated.
- Apply **realistic crypto costs** in the baseline net metrics:
  - Taker fee (e.g. 4–10 bps per side; document the rate)
  - Slippage (e.g. 1–5 bps per side or a volatility-scaled model)
- Report both **gross** and **net** results. Never claim edge on gross-only numbers.

---

## 2. Universe and processing order

1. Build a **cryptocurrency universe** suitable for hourly research (spot or perpetual—document which).
2. Rank symbols by **market capitalization descending** (use a point-in-time or dated market-cap snapshot when possible; if only a current ranking is available, document the date and the survivorship limitation).
3. Process and report results **in that market-cap order** (largest first).
4. Practical baseline filters (state defaults; adjust only with justification):
   - Minimum history: enough hourly bars for EMA100 + out-of-sample window
   - Minimum liquidity proxy (e.g. median hourly quote volume or presence on a major exchange)
   - Exclude stablecoins as quote-only bases if the tradable is `BASE/QUOTE` and BASE is a stable
5. If "all cryptocurrencies" is infeasible with available data, use the **largest N by market cap** that the data layer can support, document N, and process in descending market-cap order.

---

## 3. Research process (mandatory)

### 3.1 Before coding
- Inventory repo state: data loaders, backtest engine, existing experiments, tests.
- Write a short hypothesis card:
  - Mechanism: continuation after pullback to the faster EMA in the direction of the EMA50/EMA100 stack
  - Why it might fail: chop, fee burn, regime flips, overnight gaps, thin alts
  - Falsification: net Sharpe and trade count thresholds below; or edge disappears under modest cost stress

### 3.2 Implementation order
1. Data ingestion + integrity checks (missing bars, duplicates, timestamps, adjusted vs raw)
2. Indicator and signal unit tests on synthetic series (known cross events)
3. Single-symbol event backtest with trade log
4. Multi-symbol runner in **market-cap descending** order
5. Aggregate metrics, costs, and robustness checks
6. Persist artifacts and a next-task handoff

### 3.3 Evaluation design
- Chronological split: e.g. train/validate for any optional tuning; **final holdout untouched** until the end
- Prefer walk-forward or fixed OOS window over in-sample optimization
- Baseline uses **fixed** EMA 50/100 and 1:1 RR—no parameter search until the baseline is trustworthy
- Primary metrics (net of costs):
  - Sharpe, Sortino, max drawdown, CAGR (if equity curve)
  - Profit factor, win rate, average win/loss, trade count
  - Exposure, turnover, average holding period
  - Per-symbol and pooled results; show top/bottom symbols by market cap buckets
- Robustness (minimum set):
  - Cost stress (2× fees/slippage)
  - Conservative same-bar SL/TP path assumption
  - Subperiod stability (e.g. by year)
  - Drop top-N market-cap names (does edge rely only on BTC/ETH?)

### 3.4 Decision labels
Label the strategy as one of:
- **credible candidate** (net OOS positive with adequate trades and robustness)
- **exploratory signal** (interesting but fragile or underpowered)
- **rejected** (fails costs, stability, or sample size)
- **blocked** (data/infrastructure prevents a valid test)

Do not promote to "edge found" on in-sample performance alone.

---

## 4. Engineering and reproducibility standards

- Prefer small, testable modules: `data`, `signals`, `backtest`, `metrics`, `universe`
- Deterministic runs; seed any randomness; pin data date ranges
- Every experiment writes:
  - config (JSON/YAML)
  - trade blotter
  - equity curve or returns series
  - summary metrics table
  - commands to reproduce
- Tests must cover: EMA values on a fixed series, cross detection, SL/TP geometry, same-bar conflict rule
- Never fabricate market data, metrics, or sources
- Research/backtest only—no live trading, no secrets, no credential changes

---

## 5. Useful extensions (only after baseline is solid)

Treat these as **ordered optional mutations**, not baseline requirements:
1. Require close also above/below EMA100 for entry (stricter trend)
2. ATR-based min risk filter (skip tiny EMA100 distances)
3. Session or funding-time filters for perps
4. Portfolio-level max concurrent positions / gross exposure cap
5. Alternate RR (e.g. 1.5R) as a single controlled experiment
6. Daily trend filter on top of hourly execution

Record parent config → child config → delta metrics for each mutation.

---

## 6. Session contract (Kilo)

1. Read this file, README, any `NEXT_AGENT_TASK.md` / handoff, and existing code before changing anything.
2. Do the **smallest** change that advances a valid baseline or fixes a proven defect.
3. Run tests and report exact commands and results.
4. Persist findings; leave one narrow `NEXT_AGENT_TASK.md` with acceptance criteria and validation commands.
5. If blocked on data, make the next task "obtain/fix data for top-N market-cap crypto hourly OHLCV" rather than inventing fills.

---

## 7. Immediate objective for the first productive cycle

1. Establish hourly OHLCV access for crypto ranked by market cap (document source and N).
2. Implement EMA50/EMA100, cross entries, and 1:1 SL/TP as specified above.
3. Backtest baseline **net of costs**, process symbols in **market-cap descending** order.
4. Publish pooled and per-bucket metrics, trade counts, and a clear decision label.
5. Hand off either a robustness/mutation task or a data-blocker task with concrete criteria.

Begin by inspecting the repository state, then implement the cheapest path to a correct, cost-aware baseline of this EMA hourly continuation strategy.
