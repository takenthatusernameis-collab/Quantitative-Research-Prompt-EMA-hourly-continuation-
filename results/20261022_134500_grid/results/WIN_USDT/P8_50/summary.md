# EMA Hourly Continuation — WIN/USDT P8_50

**Symbol:** WIN/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1084 |
| net_profit_factor | 0.4282 |
| net_win_rate | 0.4336 |
| gross_profit_factor | 0.8706 |
| gross_win_rate | 0.4483 |
| sharpe_ratio | -8.7570 |
| sortino_ratio | -4.0478 |
| max_drawdown | 0.9944 |
| cagr | -0.8712 |
| net_avg_win | 15.8381 |
| net_avg_loss | -28.3155 |
| avg_hold_time_bars | 9.5950 |
| exposure | 0.4728 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
