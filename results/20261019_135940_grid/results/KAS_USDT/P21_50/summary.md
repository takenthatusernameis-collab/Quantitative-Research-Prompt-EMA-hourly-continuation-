# EMA Hourly Continuation — KAS/USDT P21_50

**Symbol:** KAS/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1038 |
| net_profit_factor | 0.3891 |
| net_win_rate | 0.4605 |
| gross_profit_factor | 0.7901 |
| gross_win_rate | 0.4711 |
| sharpe_ratio | -7.8476 |
| sortino_ratio | -3.5535 |
| max_drawdown | 0.9889 |
| cagr | -0.8319 |
| net_avg_win | 13.1756 |
| net_avg_loss | -28.9008 |
| avg_hold_time_bars | 3.9528 |
| exposure | 0.1865 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
