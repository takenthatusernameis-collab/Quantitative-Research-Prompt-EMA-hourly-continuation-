# EMA Hourly Continuation — PROM/USDT P50_200

**Symbol:** PROM/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 480 |
| net_profit_factor | 0.4162 |
| net_win_rate | 0.3896 |
| gross_profit_factor | 0.7050 |
| gross_win_rate | 0.4104 |
| sharpe_ratio | -5.9041 |
| sortino_ratio | -1.8191 |
| max_drawdown | 0.8957 |
| cagr | -0.5898 |
| net_avg_win | 34.0609 |
| net_avg_loss | -52.2276 |
| avg_hold_time_bars | 17.7417 |
| exposure | 0.3871 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
