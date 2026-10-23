# EMA Hourly Continuation — LISTA/USDT P55_100

**Symbol:** LISTA/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 560 |
| net_profit_factor | 0.4467 |
| net_win_rate | 0.4161 |
| gross_profit_factor | 0.7225 |
| gross_win_rate | 0.4375 |
| sharpe_ratio | -5.7301 |
| sortino_ratio | -1.9714 |
| max_drawdown | 0.8950 |
| cagr | -0.6177 |
| net_avg_win | 30.9726 |
| net_avg_loss | -49.4089 |
| avg_hold_time_bars | 6.8411 |
| exposure | 0.1873 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
