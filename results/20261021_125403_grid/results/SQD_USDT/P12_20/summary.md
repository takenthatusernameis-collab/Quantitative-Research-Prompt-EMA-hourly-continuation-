# EMA Hourly Continuation — SQD/USDT P12_20

**Symbol:** SQD/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 307 |
| net_profit_factor | 0.7081 |
| net_win_rate | 0.4723 |
| gross_profit_factor | 0.9157 |
| gross_win_rate | 0.4723 |
| sharpe_ratio | -2.0565 |
| sortino_ratio | -0.5221 |
| max_drawdown | 0.5000 |
| cagr | -0.2129 |
| net_avg_win | 73.7384 |
| net_avg_loss | -93.2137 |
| avg_hold_time_bars | 4.9381 |
| exposure | 0.0713 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
