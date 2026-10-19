# EMA Hourly Continuation — CVX/USDT P20_21

**Symbol:** CVX/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1218 |
| net_profit_factor | 0.1551 |
| net_win_rate | 0.3103 |
| gross_profit_factor | 0.6944 |
| gross_win_rate | 0.3867 |
| sharpe_ratio | -16.8074 |
| sortino_ratio | -8.7457 |
| max_drawdown | 1.0000 |
| cagr | -0.9925 |
| net_avg_win | 4.8560 |
| net_avg_loss | -14.0899 |
| avg_hold_time_bars | 1.8998 |
| exposure | 0.1052 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
