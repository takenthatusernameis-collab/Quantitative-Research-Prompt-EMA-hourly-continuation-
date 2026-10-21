# EMA Hourly Continuation — SEI/USDT P12_26

**Symbol:** SEI/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 432 |
| net_profit_factor | 0.7512 |
| net_win_rate | 0.4977 |
| gross_profit_factor | 1.0125 |
| gross_win_rate | 0.4977 |
| sharpe_ratio | -2.0680 |
| sortino_ratio | -0.6166 |
| max_drawdown | 0.5377 |
| cagr | -0.2465 |
| net_avg_win | 71.4291 |
| net_avg_loss | -94.2115 |
| avg_hold_time_bars | 5.5301 |
| exposure | 0.1086 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
