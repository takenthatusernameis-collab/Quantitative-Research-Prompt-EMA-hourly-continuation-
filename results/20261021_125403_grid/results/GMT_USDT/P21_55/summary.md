# EMA Hourly Continuation — GMT/USDT P21_55

**Symbol:** GMT/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 511 |
| net_profit_factor | 0.7059 |
| net_win_rate | 0.4873 |
| gross_profit_factor | 0.9434 |
| gross_win_rate | 0.4873 |
| sharpe_ratio | -2.4043 |
| sortino_ratio | -0.7780 |
| max_drawdown | 0.6084 |
| cagr | -0.2998 |
| net_avg_win | 57.0093 |
| net_avg_loss | -76.7510 |
| avg_hold_time_bars | 7.9863 |
| exposure | 0.1855 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
