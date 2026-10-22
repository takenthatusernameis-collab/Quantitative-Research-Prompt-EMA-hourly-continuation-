# EMA Hourly Continuation — MAGIC/USDT P26_200

**Symbol:** MAGIC/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 306 |
| net_profit_factor | 0.7997 |
| net_win_rate | 0.4935 |
| gross_profit_factor | 0.9828 |
| gross_win_rate | 0.4935 |
| sharpe_ratio | -1.3030 |
| sortino_ratio | -0.3255 |
| max_drawdown | 0.4035 |
| cagr | -0.1406 |
| net_avg_win | 83.6660 |
| net_avg_loss | -101.9275 |
| avg_hold_time_bars | 42.9510 |
| exposure | 0.5974 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
