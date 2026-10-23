# EMA Hourly Continuation — FIDA/USDT P55_200

**Symbol:** FIDA/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 410 |
| net_profit_factor | 0.5286 |
| net_win_rate | 0.4366 |
| gross_profit_factor | 0.7803 |
| gross_win_rate | 0.4390 |
| sharpe_ratio | -3.8606 |
| sortino_ratio | -1.0855 |
| max_drawdown | 0.7451 |
| cagr | -0.4136 |
| net_avg_win | 46.3539 |
| net_avg_loss | -67.9471 |
| avg_hold_time_bars | 20.2195 |
| exposure | 0.3751 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
