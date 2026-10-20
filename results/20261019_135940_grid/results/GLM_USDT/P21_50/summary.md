# EMA Hourly Continuation — GLM/USDT P21_50

**Symbol:** GLM/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 907 |
| net_profit_factor | 0.4052 |
| net_win_rate | 0.4498 |
| gross_profit_factor | 0.7574 |
| gross_win_rate | 0.4642 |
| sharpe_ratio | -7.2602 |
| sortino_ratio | -3.0786 |
| max_drawdown | 0.9780 |
| cagr | -0.7795 |
| net_avg_win | 16.3188 |
| net_avg_loss | -32.9331 |
| avg_hold_time_bars | 5.7773 |
| exposure | 0.2382 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
