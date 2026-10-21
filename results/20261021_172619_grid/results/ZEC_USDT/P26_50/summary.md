# EMA Hourly Continuation — ZEC/USDT P26_50

**Symbol:** ZEC/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 339 |
| net_profit_factor | 0.9034 |
| net_win_rate | 0.5398 |
| gross_profit_factor | 1.1721 |
| gross_win_rate | 0.5398 |
| sharpe_ratio | -0.5725 |
| sortino_ratio | -0.1525 |
| max_drawdown | 0.2390 |
| cagr | -0.0710 |
| net_avg_win | 86.3560 |
| net_avg_loss | -112.1305 |
| avg_hold_time_bars | 6.3746 |
| exposure | 0.0982 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
