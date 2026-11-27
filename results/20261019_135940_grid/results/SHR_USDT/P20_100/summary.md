# EMA Hourly Continuation — SHR/USDT P20_100

**Symbol:** SHR/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 997 |
| net_profit_factor | 0.4212 |
| net_win_rate | 0.3430 |
| gross_profit_factor | 0.5771 |
| gross_win_rate | 0.3450 |
| sharpe_ratio | -8.9769 |
| sortino_ratio | -3.9550 |
| max_drawdown | 0.9917 |
| cagr | -0.8493 |
| net_avg_win | 21.0970 |
| net_avg_loss | -26.1537 |
| avg_hold_time_bars | 7.7653 |
| exposure | 0.3503 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
