# EMA Hourly Continuation — CHR/USDT P20_50

**Symbol:** CHR/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 569 |
| net_profit_factor | 0.6854 |
| net_win_rate | 0.4692 |
| gross_profit_factor | 0.8937 |
| gross_win_rate | 0.4692 |
| sharpe_ratio | -2.9140 |
| sortino_ratio | -0.9890 |
| max_drawdown | 0.6897 |
| cagr | -0.3641 |
| net_avg_win | 55.5461 |
| net_avg_loss | -71.6540 |
| avg_hold_time_bars | 7.6749 |
| exposure | 0.1976 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
