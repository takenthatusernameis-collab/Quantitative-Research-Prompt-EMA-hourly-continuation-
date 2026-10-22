# EMA Hourly Continuation — OP/USDT P20_34

**Symbol:** OP/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1147 |
| net_profit_factor | 0.3281 |
| net_win_rate | 0.4228 |
| gross_profit_factor | 0.7736 |
| gross_win_rate | 0.4377 |
| sharpe_ratio | -10.2333 |
| sortino_ratio | -4.9205 |
| max_drawdown | 0.9980 |
| cagr | -0.9155 |
| net_avg_win | 10.0488 |
| net_avg_loss | -22.4373 |
| avg_hold_time_bars | 2.4542 |
| exposure | 0.1280 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
