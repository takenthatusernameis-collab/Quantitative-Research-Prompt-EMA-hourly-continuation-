# EMA Hourly Continuation — DBR/USDT P21_34

**Symbol:** DBR/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 728 |
| net_profit_factor | 0.4339 |
| net_win_rate | 0.4245 |
| gross_profit_factor | 1.0476 |
| gross_win_rate | 0.4725 |
| sharpe_ratio | -9.3590 |
| sortino_ratio | -4.0196 |
| max_drawdown | 0.9834 |
| cagr | -0.8702 |
| net_avg_win | 24.3907 |
| net_avg_loss | -41.4574 |
| avg_hold_time_bars | 4.1552 |
| exposure | 0.1720 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
