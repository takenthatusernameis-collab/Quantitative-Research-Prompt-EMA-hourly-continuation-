# EMA Hourly Continuation — SKY/USDT P21_55

**Symbol:** SKY/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 460 |
| net_profit_factor | 0.6637 |
| net_win_rate | 0.4826 |
| gross_profit_factor | 0.9265 |
| gross_win_rate | 0.4826 |
| sharpe_ratio | -3.0682 |
| sortino_ratio | -1.0415 |
| max_drawdown | 0.6374 |
| cagr | -0.3805 |
| net_avg_win | 55.5453 |
| net_avg_loss | -78.0643 |
| avg_hold_time_bars | 8.5630 |
| exposure | 0.2196 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
