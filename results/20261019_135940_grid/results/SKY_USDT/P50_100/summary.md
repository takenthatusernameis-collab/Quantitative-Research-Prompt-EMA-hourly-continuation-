# EMA Hourly Continuation — SKY/USDT P50_100

**Symbol:** SKY/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 525 |
| net_profit_factor | 0.5698 |
| net_win_rate | 0.4857 |
| gross_profit_factor | 1.0307 |
| gross_win_rate | 0.5029 |
| sharpe_ratio | -4.8853 |
| sortino_ratio | -1.7224 |
| max_drawdown | 0.8422 |
| cagr | -0.5809 |
| net_avg_win | 43.1835 |
| net_avg_loss | -71.5761 |
| avg_hold_time_bars | 6.1467 |
| exposure | 0.1799 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
