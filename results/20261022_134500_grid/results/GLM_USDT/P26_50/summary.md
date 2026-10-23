# EMA Hourly Continuation — GLM/USDT P26_50

**Symbol:** GLM/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 898 |
| net_profit_factor | 0.3810 |
| net_win_rate | 0.4521 |
| gross_profit_factor | 0.7426 |
| gross_win_rate | 0.4699 |
| sharpe_ratio | -7.3545 |
| sortino_ratio | -3.1236 |
| max_drawdown | 0.9782 |
| cagr | -0.7811 |
| net_avg_win | 14.8249 |
| net_avg_loss | -32.1109 |
| avg_hold_time_bars | 4.7105 |
| exposure | 0.1923 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
