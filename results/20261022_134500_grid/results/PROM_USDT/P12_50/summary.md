# EMA Hourly Continuation — PROM/USDT P12_50

**Symbol:** PROM/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1061 |
| net_profit_factor | 0.5294 |
| net_win_rate | 0.4147 |
| gross_profit_factor | 0.9075 |
| gross_win_rate | 0.4420 |
| sharpe_ratio | -8.2650 |
| sortino_ratio | -3.7711 |
| max_drawdown | 0.9907 |
| cagr | -0.8446 |
| net_avg_win | 25.3271 |
| net_avg_loss | -33.8981 |
| avg_hold_time_bars | 8.0745 |
| exposure | 0.3894 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
