# EMA Hourly Continuation — ANKR/USDT P34_100

**Symbol:** ANKR/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 478 |
| net_profit_factor | 0.6098 |
| net_win_rate | 0.4372 |
| gross_profit_factor | 0.8172 |
| gross_win_rate | 0.4372 |
| sharpe_ratio | -3.8655 |
| sortino_ratio | -1.2013 |
| max_drawdown | 0.7550 |
| cagr | -0.4267 |
| net_avg_win | 56.2700 |
| net_avg_loss | -71.6988 |
| avg_hold_time_bars | 13.5816 |
| exposure | 0.2951 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
