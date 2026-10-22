# EMA Hourly Continuation — CHZ/USDT P89_100

**Symbol:** CHZ/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 604 |
| net_profit_factor | 0.2478 |
| net_win_rate | 0.3825 |
| gross_profit_factor | 0.7408 |
| gross_win_rate | 0.4288 |
| sharpe_ratio | -9.5404 |
| sortino_ratio | -3.4534 |
| max_drawdown | 0.9872 |
| cagr | -0.8231 |
| net_avg_win | 14.0809 |
| net_avg_loss | -35.1840 |
| avg_hold_time_bars | 1.9238 |
| exposure | 0.0528 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
