# EMA Hourly Continuation — DCR/USDT P21_55

**Symbol:** DCR/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 580 |
| net_profit_factor | 0.6110 |
| net_win_rate | 0.4741 |
| gross_profit_factor | 0.8611 |
| gross_win_rate | 0.4741 |
| sharpe_ratio | -3.2981 |
| sortino_ratio | -1.1309 |
| max_drawdown | 0.7512 |
| cagr | -0.4066 |
| net_avg_win | 41.7972 |
| net_avg_loss | -61.6822 |
| avg_hold_time_bars | 8.3052 |
| exposure | 0.2180 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
