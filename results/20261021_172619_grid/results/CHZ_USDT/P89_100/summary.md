# EMA Hourly Continuation — CHZ/USDT P89_100

**Symbol:** CHZ/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 79 |
| net_profit_factor | 0.4665 |
| net_win_rate | 0.4051 |
| gross_profit_factor | 0.6884 |
| gross_win_rate | 0.4051 |
| sharpe_ratio | -2.0840 |
| sortino_ratio | -0.2644 |
| max_drawdown | 0.2755 |
| cagr | -0.1146 |
| net_avg_win | 71.9582 |
| net_avg_loss | -105.0251 |
| avg_hold_time_bars | 4.2658 |
| exposure | 0.0153 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
