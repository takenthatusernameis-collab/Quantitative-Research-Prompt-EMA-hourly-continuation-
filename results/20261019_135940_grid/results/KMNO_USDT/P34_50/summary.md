# EMA Hourly Continuation — KMNO/USDT P34_50

**Symbol:** KMNO/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 801 |
| net_profit_factor | 0.4902 |
| net_win_rate | 0.4532 |
| gross_profit_factor | 0.9449 |
| gross_win_rate | 0.4769 |
| sharpe_ratio | -7.3063 |
| sortino_ratio | -2.9549 |
| max_drawdown | 0.9739 |
| cagr | -0.7692 |
| net_avg_win | 25.7869 |
| net_avg_loss | -43.5941 |
| avg_hold_time_bars | 2.8327 |
| exposure | 0.1048 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
