# EMA Hourly Continuation — ETC/USDT P21_50

**Symbol:** ETC/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 995 |
| net_profit_factor | 0.3564 |
| net_win_rate | 0.4211 |
| gross_profit_factor | 0.8143 |
| gross_win_rate | 0.4472 |
| sharpe_ratio | -9.9032 |
| sortino_ratio | -4.4228 |
| max_drawdown | 0.9967 |
| cagr | -0.8958 |
| net_avg_win | 13.1730 |
| net_avg_loss | -26.8841 |
| avg_hold_time_bars | 4.6231 |
| exposure | 0.2091 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
