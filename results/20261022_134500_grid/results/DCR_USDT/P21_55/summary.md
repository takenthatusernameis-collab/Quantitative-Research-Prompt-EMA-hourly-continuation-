# EMA Hourly Continuation — DCR/USDT P21_55

**Symbol:** DCR/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 999 |
| net_profit_factor | 0.4563 |
| net_win_rate | 0.4324 |
| gross_profit_factor | 0.8109 |
| gross_win_rate | 0.4535 |
| sharpe_ratio | -7.8267 |
| sortino_ratio | -3.4906 |
| max_drawdown | 0.9873 |
| cagr | -0.8192 |
| net_avg_win | 19.1688 |
| net_avg_loss | -32.0056 |
| avg_hold_time_bars | 5.7177 |
| exposure | 0.2585 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
