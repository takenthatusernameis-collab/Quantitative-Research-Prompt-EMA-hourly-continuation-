# EMA Hourly Continuation — ANKR/USDT P20_144

**Symbol:** ANKR/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 484 |
| net_profit_factor | 0.6064 |
| net_win_rate | 0.4463 |
| gross_profit_factor | 0.9218 |
| gross_win_rate | 0.4628 |
| sharpe_ratio | -3.9871 |
| sortino_ratio | -1.2232 |
| max_drawdown | 0.7824 |
| cagr | -0.4518 |
| net_avg_win | 55.5737 |
| net_avg_loss | -73.8580 |
| avg_hold_time_bars | 26.9773 |
| exposure | 0.5935 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
