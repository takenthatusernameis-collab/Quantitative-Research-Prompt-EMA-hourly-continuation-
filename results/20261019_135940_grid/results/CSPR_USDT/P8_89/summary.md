# EMA Hourly Continuation — CSPR/USDT P8_89

**Symbol:** CSPR/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 987 |
| net_profit_factor | 0.4364 |
| net_win_rate | 0.4134 |
| gross_profit_factor | 0.7350 |
| gross_win_rate | 0.4245 |
| sharpe_ratio | -7.3633 |
| sortino_ratio | -3.2458 |
| max_drawdown | 0.9816 |
| cagr | -0.7942 |
| net_avg_win | 18.6209 |
| net_avg_loss | -30.0664 |
| avg_hold_time_bars | 13.2482 |
| exposure | 0.5944 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
