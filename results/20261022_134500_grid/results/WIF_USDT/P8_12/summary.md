# EMA Hourly Continuation — WIF/USDT P8_12

**Symbol:** WIF/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1787 |
| net_profit_factor | 0.3735 |
| net_win_rate | 0.3844 |
| gross_profit_factor | 0.7811 |
| gross_win_rate | 0.4180 |
| sharpe_ratio | -15.4517 |
| sortino_ratio | -9.3243 |
| max_drawdown | 1.0000 |
| cagr | -0.9923 |
| net_avg_win | 8.6791 |
| net_avg_loss | -14.5114 |
| avg_hold_time_bars | 1.7510 |
| exposure | 0.1422 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
