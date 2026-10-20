# EMA Hourly Continuation — RSR/USDT P50_100

**Symbol:** RSR/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 631 |
| net_profit_factor | 0.5754 |
| net_win_rate | 0.4707 |
| gross_profit_factor | 0.8904 |
| gross_win_rate | 0.4770 |
| sharpe_ratio | -4.1280 |
| sortino_ratio | -1.4631 |
| max_drawdown | 0.8300 |
| cagr | -0.5029 |
| net_avg_win | 37.7401 |
| net_avg_loss | -58.3231 |
| avg_hold_time_bars | 6.0174 |
| exposure | 0.1726 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
