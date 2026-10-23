# EMA Hourly Continuation — MOCA/USDT P34_55

**Symbol:** MOCA/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 799 |
| net_profit_factor | 0.3824 |
| net_win_rate | 0.4068 |
| gross_profit_factor | 0.7501 |
| gross_win_rate | 0.4330 |
| sharpe_ratio | -8.9496 |
| sortino_ratio | -3.7521 |
| max_drawdown | 0.9871 |
| cagr | -0.8502 |
| net_avg_win | 18.7963 |
| net_avg_loss | -33.7051 |
| avg_hold_time_bars | 3.5282 |
| exposure | 0.1413 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
