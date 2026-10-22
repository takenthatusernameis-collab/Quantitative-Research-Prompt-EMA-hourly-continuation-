# EMA Hourly Continuation — SNX/USDT P20_34

**Symbol:** SNX/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1149 |
| net_profit_factor | 0.4119 |
| net_win_rate | 0.4604 |
| gross_profit_factor | 0.9165 |
| gross_win_rate | 0.4891 |
| sharpe_ratio | -8.6054 |
| sortino_ratio | -4.1156 |
| max_drawdown | 0.9942 |
| cagr | -0.8696 |
| net_avg_win | 13.1604 |
| net_avg_loss | -27.2633 |
| avg_hold_time_bars | 2.6423 |
| exposure | 0.1374 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
