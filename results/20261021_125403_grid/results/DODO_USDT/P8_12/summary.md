# EMA Hourly Continuation — DODO/USDT P8_12

**Symbol:** DODO/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 429 |
| net_profit_factor | 0.5578 |
| net_win_rate | 0.4382 |
| gross_profit_factor | 0.8118 |
| gross_win_rate | 0.4382 |
| sharpe_ratio | -4.0223 |
| sortino_ratio | -1.1867 |
| max_drawdown | 0.7504 |
| cagr | -0.4211 |
| net_avg_win | 50.1939 |
| net_avg_loss | -70.1981 |
| avg_hold_time_bars | 4.7762 |
| exposure | 0.0927 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
