# EMA Hourly Continuation — FLOW/USDT P26_144

**Symbol:** FLOW/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 350 |
| net_profit_factor | 0.7553 |
| net_win_rate | 0.4829 |
| gross_profit_factor | 0.9319 |
| gross_win_rate | 0.4829 |
| sharpe_ratio | -1.6703 |
| sortino_ratio | -0.4451 |
| max_drawdown | 0.4288 |
| cagr | -0.1860 |
| net_avg_win | 73.6873 |
| net_avg_loss | -91.0973 |
| avg_hold_time_bars | 31.6571 |
| exposure | 0.5036 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
