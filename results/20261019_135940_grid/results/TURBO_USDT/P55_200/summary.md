# EMA Hourly Continuation — TURBO/USDT P55_200

**Symbol:** TURBO/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 353 |
| net_profit_factor | 0.7986 |
| net_win_rate | 0.5156 |
| gross_profit_factor | 1.0958 |
| gross_win_rate | 0.5212 |
| sharpe_ratio | -1.5247 |
| sortino_ratio | -0.4467 |
| max_drawdown | 0.3789 |
| cagr | -0.1904 |
| net_avg_win | 77.8391 |
| net_avg_loss | -103.7413 |
| avg_hold_time_bars | 17.8980 |
| exposure | 0.3447 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
