# EMA Hourly Continuation — ZEN/USDT P26_50

**Symbol:** ZEN/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 439 |
| net_profit_factor | 0.6626 |
| net_win_rate | 0.4738 |
| gross_profit_factor | 0.8960 |
| gross_win_rate | 0.4738 |
| sharpe_ratio | -2.6928 |
| sortino_ratio | -0.8060 |
| max_drawdown | 0.6243 |
| cagr | -0.3098 |
| net_avg_win | 57.2180 |
| net_avg_loss | -77.7513 |
| avg_hold_time_bars | 6.0911 |
| exposure | 0.1215 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
