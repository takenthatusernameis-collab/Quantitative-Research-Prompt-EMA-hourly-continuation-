# EMA Hourly Continuation — API3/USDT P21_50

**Symbol:** API3/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 542 |
| net_profit_factor | 0.7309 |
| net_win_rate | 0.4908 |
| gross_profit_factor | 0.9812 |
| gross_win_rate | 0.4908 |
| sharpe_ratio | -2.5323 |
| sortino_ratio | -0.8436 |
| max_drawdown | 0.6285 |
| cagr | -0.3211 |
| net_avg_win | 63.4870 |
| net_avg_loss | -83.7193 |
| avg_hold_time_bars | 7.2103 |
| exposure | 0.1776 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
