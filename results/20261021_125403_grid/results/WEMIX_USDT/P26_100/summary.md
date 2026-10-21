# EMA Hourly Continuation — WEMIX/USDT P26_100

**Symbol:** WEMIX/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 379 |
| net_profit_factor | 0.5543 |
| net_win_rate | 0.4011 |
| gross_profit_factor | 0.7028 |
| gross_win_rate | 0.4011 |
| sharpe_ratio | -3.9236 |
| sortino_ratio | -1.0785 |
| max_drawdown | 0.7201 |
| cagr | -0.3934 |
| net_avg_win | 58.5047 |
| net_avg_loss | -70.6715 |
| avg_hold_time_bars | 22.9525 |
| exposure | 0.3954 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
