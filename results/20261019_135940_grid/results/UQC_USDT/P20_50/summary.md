# EMA Hourly Continuation — UQC/USDT P20_50

**Symbol:** UQC/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 422 |
| net_profit_factor | 0.1613 |
| net_win_rate | 0.2820 |
| gross_profit_factor | 0.4104 |
| gross_win_rate | 0.3081 |
| sharpe_ratio | -8.6981 |
| sortino_ratio | -2.5354 |
| max_drawdown | 0.9666 |
| cagr | -0.7401 |
| net_avg_win | 15.6222 |
| net_avg_loss | -38.0352 |
| avg_hold_time_bars | 28.3081 |
| exposure | 0.5407 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
