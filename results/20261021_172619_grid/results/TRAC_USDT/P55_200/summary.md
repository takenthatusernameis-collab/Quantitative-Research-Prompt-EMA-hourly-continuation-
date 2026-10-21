# EMA Hourly Continuation — TRAC/USDT P55_200

**Symbol:** TRAC/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 326 |
| net_profit_factor | 0.7923 |
| net_win_rate | 0.4969 |
| gross_profit_factor | 0.9743 |
| gross_win_rate | 0.4969 |
| sharpe_ratio | -1.2686 |
| sortino_ratio | -0.3271 |
| max_drawdown | 0.3308 |
| cagr | -0.1403 |
| net_avg_win | 74.3989 |
| net_avg_loss | -92.7551 |
| avg_hold_time_bars | 21.4325 |
| exposure | 0.3176 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
