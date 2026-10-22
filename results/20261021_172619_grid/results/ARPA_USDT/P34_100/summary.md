# EMA Hourly Continuation — ARPA/USDT P34_100

**Symbol:** ARPA/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 506 |
| net_profit_factor | 0.5918 |
| net_win_rate | 0.4447 |
| gross_profit_factor | 0.7971 |
| gross_win_rate | 0.4447 |
| sharpe_ratio | -3.7548 |
| sortino_ratio | -1.1982 |
| max_drawdown | 0.7678 |
| cagr | -0.4236 |
| net_avg_win | 48.3820 |
| net_avg_loss | -65.4621 |
| avg_hold_time_bars | 11.9486 |
| exposure | 0.2736 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
