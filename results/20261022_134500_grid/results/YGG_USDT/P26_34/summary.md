# EMA Hourly Continuation — YGG/USDT P26_34

**Symbol:** YGG/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1098 |
| net_profit_factor | 0.3963 |
| net_win_rate | 0.4162 |
| gross_profit_factor | 0.8391 |
| gross_win_rate | 0.4526 |
| sharpe_ratio | -10.5531 |
| sortino_ratio | -4.9943 |
| max_drawdown | 0.9982 |
| cagr | -0.9176 |
| net_avg_win | 14.3404 |
| net_avg_loss | -25.7958 |
| avg_hold_time_bars | 2.2004 |
| exposure | 0.1093 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
