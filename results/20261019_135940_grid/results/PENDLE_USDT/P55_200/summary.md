# EMA Hourly Continuation — PENDLE/USDT P55_200

**Symbol:** PENDLE/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 370 |
| net_profit_factor | 0.7400 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9990 |
| gross_win_rate | 0.5027 |
| sharpe_ratio | -1.7390 |
| sortino_ratio | -0.4721 |
| max_drawdown | 0.4391 |
| cagr | -0.2017 |
| net_avg_win | 66.4757 |
| net_avg_loss | -89.8315 |
| avg_hold_time_bars | 25.0297 |
| exposure | 0.4210 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
