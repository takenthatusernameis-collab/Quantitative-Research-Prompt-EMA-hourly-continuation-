# EMA Hourly Continuation — LUNC/USDT P50_100

**Symbol:** LUNC/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 337 |
| net_profit_factor | 0.8084 |
| net_win_rate | 0.5282 |
| gross_profit_factor | 1.0944 |
| gross_win_rate | 0.5282 |
| sharpe_ratio | -1.0916 |
| sortino_ratio | -0.2893 |
| max_drawdown | 0.3078 |
| cagr | -0.1250 |
| net_avg_win | 67.5118 |
| net_avg_loss | -93.4957 |
| avg_hold_time_bars | 9.5697 |
| exposure | 0.1466 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
