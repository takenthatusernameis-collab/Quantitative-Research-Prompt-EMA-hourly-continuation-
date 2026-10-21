# EMA Hourly Continuation — LQTY/USDT P34_100

**Symbol:** LQTY/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 451 |
| net_profit_factor | 0.6992 |
| net_win_rate | 0.4723 |
| gross_profit_factor | 0.8900 |
| gross_win_rate | 0.4723 |
| sharpe_ratio | -2.4157 |
| sortino_ratio | -0.7292 |
| max_drawdown | 0.5827 |
| cagr | -0.2847 |
| net_avg_win | 62.2692 |
| net_avg_loss | -79.7019 |
| avg_hold_time_bars | 13.8891 |
| exposure | 0.2835 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
