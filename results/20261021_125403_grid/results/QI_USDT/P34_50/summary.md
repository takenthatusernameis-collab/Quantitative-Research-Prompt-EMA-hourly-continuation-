# EMA Hourly Continuation — QI/USDT P34_50

**Symbol:** QI/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 374 |
| net_profit_factor | 0.7830 |
| net_win_rate | 0.5455 |
| gross_profit_factor | 1.2186 |
| gross_win_rate | 0.5455 |
| sharpe_ratio | -1.5710 |
| sortino_ratio | -0.4396 |
| max_drawdown | 0.4544 |
| cagr | -0.1809 |
| net_avg_win | 69.9659 |
| net_avg_loss | -107.2209 |
| avg_hold_time_bars | 4.6096 |
| exposure | 0.0780 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
