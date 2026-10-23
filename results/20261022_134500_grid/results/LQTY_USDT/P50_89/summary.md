# EMA Hourly Continuation — LQTY/USDT P50_89

**Symbol:** LQTY/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 706 |
| net_profit_factor | 0.4420 |
| net_win_rate | 0.4235 |
| gross_profit_factor | 0.7436 |
| gross_win_rate | 0.4348 |
| sharpe_ratio | -6.6730 |
| sortino_ratio | -2.4968 |
| max_drawdown | 0.9530 |
| cagr | -0.7012 |
| net_avg_win | 25.2359 |
| net_avg_loss | -41.9425 |
| avg_hold_time_bars | 4.9306 |
| exposure | 0.1575 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
