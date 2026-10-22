# EMA Hourly Continuation — PEPE/USDT P50_144

**Symbol:** PEPE/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 496 |
| net_profit_factor | 0.5958 |
| net_win_rate | 0.4617 |
| gross_profit_factor | 0.8719 |
| gross_win_rate | 0.4637 |
| sharpe_ratio | -3.8823 |
| sortino_ratio | -1.2213 |
| max_drawdown | 0.7692 |
| cagr | -0.4406 |
| net_avg_win | 49.4000 |
| net_avg_loss | -71.1122 |
| avg_hold_time_bars | 13.4798 |
| exposure | 0.3039 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
