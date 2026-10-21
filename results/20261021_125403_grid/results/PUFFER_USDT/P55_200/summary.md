# EMA Hourly Continuation — PUFFER/USDT P55_200

**Symbol:** PUFFER/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 236 |
| net_profit_factor | 0.8380 |
| net_win_rate | 0.4958 |
| gross_profit_factor | 0.9815 |
| gross_win_rate | 0.4958 |
| sharpe_ratio | -0.9125 |
| sortino_ratio | -0.2236 |
| max_drawdown | 0.2751 |
| cagr | -0.0997 |
| net_avg_win | 84.4062 |
| net_avg_loss | -99.0268 |
| avg_hold_time_bars | 26.0297 |
| exposure | 0.3476 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
