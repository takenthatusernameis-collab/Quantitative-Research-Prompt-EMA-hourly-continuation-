# EMA Hourly Continuation — HTX/USDT P20_34

**Symbol:** HTX/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 426 |
| net_profit_factor | 0.2948 |
| net_win_rate | 0.3333 |
| gross_profit_factor | 0.5708 |
| gross_win_rate | 0.3427 |
| sharpe_ratio | -8.0998 |
| sortino_ratio | -2.4541 |
| max_drawdown | 0.9478 |
| cagr | -0.6899 |
| net_avg_win | 27.9070 |
| net_avg_loss | -47.3275 |
| avg_hold_time_bars | 6.2488 |
| exposure | 0.1205 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
