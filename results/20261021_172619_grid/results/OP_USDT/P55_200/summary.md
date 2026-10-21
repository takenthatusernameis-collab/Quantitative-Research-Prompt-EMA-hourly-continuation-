# EMA Hourly Continuation — OP/USDT P55_200

**Symbol:** OP/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 284 |
| net_profit_factor | 0.7958 |
| net_win_rate | 0.4894 |
| gross_profit_factor | 0.9611 |
| gross_win_rate | 0.4894 |
| sharpe_ratio | -1.2248 |
| sortino_ratio | -0.2948 |
| max_drawdown | 0.3256 |
| cagr | -0.1276 |
| net_avg_win | 81.3751 |
| net_avg_loss | -98.0223 |
| avg_hold_time_bars | 28.7289 |
| exposure | 0.3709 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
