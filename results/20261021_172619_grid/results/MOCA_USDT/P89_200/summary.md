# EMA Hourly Continuation — MOCA/USDT P89_200

**Symbol:** MOCA/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 240 |
| net_profit_factor | 0.6881 |
| net_win_rate | 0.4667 |
| gross_profit_factor | 0.8698 |
| gross_win_rate | 0.4667 |
| sharpe_ratio | -1.8987 |
| sortino_ratio | -0.4395 |
| max_drawdown | 0.3697 |
| cagr | -0.1833 |
| net_avg_win | 72.7755 |
| net_avg_loss | -92.5372 |
| avg_hold_time_bars | 15.6167 |
| exposure | 0.1879 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
