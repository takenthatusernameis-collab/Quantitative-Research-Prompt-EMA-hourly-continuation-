# EMA Hourly Continuation — SHR/USDT P20_200

**Symbol:** SHR/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 686 |
| net_profit_factor | 0.5276 |
| net_win_rate | 0.3746 |
| gross_profit_factor | 0.6704 |
| gross_win_rate | 0.3746 |
| sharpe_ratio | -5.9836 |
| sortino_ratio | -2.1737 |
| max_drawdown | 0.9312 |
| cagr | -0.6463 |
| net_avg_win | 40.2982 |
| net_avg_loss | -45.7567 |
| avg_hold_time_bars | 16.7128 |
| exposure | 0.5188 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
