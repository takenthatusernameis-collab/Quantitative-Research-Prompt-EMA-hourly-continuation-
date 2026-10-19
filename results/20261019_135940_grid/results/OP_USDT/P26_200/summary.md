# EMA Hourly Continuation — OP/USDT P26_200

**Symbol:** OP/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 332 |
| net_profit_factor | 0.6047 |
| net_win_rate | 0.4488 |
| gross_profit_factor | 0.8408 |
| gross_win_rate | 0.4578 |
| sharpe_ratio | -2.8677 |
| sortino_ratio | -0.7276 |
| max_drawdown | 0.5862 |
| cagr | -0.2956 |
| net_avg_win | 60.1006 |
| net_avg_loss | -80.9169 |
| avg_hold_time_bars | 40.4639 |
| exposure | 0.6106 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
