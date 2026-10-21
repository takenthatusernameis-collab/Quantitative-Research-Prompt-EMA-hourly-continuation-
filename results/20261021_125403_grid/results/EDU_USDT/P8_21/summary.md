# EMA Hourly Continuation — EDU/USDT P8_21

**Symbol:** EDU/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 718 |
| net_profit_factor | 0.6895 |
| net_win_rate | 0.4847 |
| gross_profit_factor | 0.9460 |
| gross_win_rate | 0.4847 |
| sharpe_ratio | -3.1243 |
| sortino_ratio | -1.1947 |
| max_drawdown | 0.7531 |
| cagr | -0.4213 |
| net_avg_win | 47.7567 |
| net_avg_loss | -65.1447 |
| avg_hold_time_bars | 5.9095 |
| exposure | 0.1920 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
