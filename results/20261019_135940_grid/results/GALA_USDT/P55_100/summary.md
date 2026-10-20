# EMA Hourly Continuation — GALA/USDT P55_100

**Symbol:** GALA/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 637 |
| net_profit_factor | 0.4819 |
| net_win_rate | 0.4301 |
| gross_profit_factor | 0.7912 |
| gross_win_rate | 0.4380 |
| sharpe_ratio | -5.8701 |
| sortino_ratio | -2.0848 |
| max_drawdown | 0.9246 |
| cagr | -0.6389 |
| net_avg_win | 31.3203 |
| net_avg_loss | -49.0554 |
| avg_hold_time_bars | 5.7206 |
| exposure | 0.1656 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
