# EMA Hourly Continuation — BTC/USDT P8_34

**Symbol:** BTC/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 765 |
| net_profit_factor | 0.5681 |
| net_win_rate | 0.4967 |
| gross_profit_factor | 0.9774 |
| gross_win_rate | 0.5059 |
| sharpe_ratio | -4.5470 |
| sortino_ratio | -1.7011 |
| max_drawdown | 0.8919 |
| cagr | -0.5414 |
| net_avg_win | 30.8743 |
| net_avg_loss | -53.6394 |
| avg_hold_time_bars | 10.1359 |
| exposure | 0.3102 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
