# EMA Hourly Continuation — ETC/USDT P26_100

**Symbol:** ETC/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 665 |
| net_profit_factor | 0.4909 |
| net_win_rate | 0.4677 |
| gross_profit_factor | 0.9664 |
| gross_win_rate | 0.4842 |
| sharpe_ratio | -5.7638 |
| sortino_ratio | -2.0754 |
| max_drawdown | 0.9300 |
| cagr | -0.6459 |
| net_avg_win | 28.7150 |
| net_avg_loss | -51.3923 |
| avg_hold_time_bars | 11.1594 |
| exposure | 0.3373 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
