# EMA Hourly Continuation — CAKE/USDT P55_200

**Symbol:** CAKE/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 285 |
| net_profit_factor | 0.8017 |
| net_win_rate | 0.5193 |
| gross_profit_factor | 1.0455 |
| gross_win_rate | 0.5193 |
| sharpe_ratio | -1.0429 |
| sortino_ratio | -0.2524 |
| max_drawdown | 0.3294 |
| cagr | -0.1110 |
| net_avg_win | 69.8603 |
| net_avg_loss | -94.1398 |
| avg_hold_time_bars | 24.9368 |
| exposure | 0.3230 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
