# EMA Hourly Continuation — SKY/USDT P12_50

**Symbol:** SKY/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 855 |
| net_profit_factor | 0.5501 |
| net_win_rate | 0.4667 |
| gross_profit_factor | 0.9473 |
| gross_win_rate | 0.4819 |
| sharpe_ratio | -6.5646 |
| sortino_ratio | -2.9811 |
| max_drawdown | 0.9498 |
| cagr | -0.7671 |
| net_avg_win | 29.0973 |
| net_avg_loss | -46.2794 |
| avg_hold_time_bars | 7.5006 |
| exposure | 0.3576 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
