# EMA Hourly Continuation — NYM/USDT P8_55

**Symbol:** NYM/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 455 |
| net_profit_factor | 0.5603 |
| net_win_rate | 0.4374 |
| gross_profit_factor | 0.7983 |
| gross_win_rate | 0.4374 |
| sharpe_ratio | -3.9843 |
| sortino_ratio | -1.2044 |
| max_drawdown | 0.7672 |
| cagr | -0.4282 |
| net_avg_win | 48.3087 |
| net_avg_loss | -67.0186 |
| avg_hold_time_bars | 27.8901 |
| exposure | 0.5768 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
