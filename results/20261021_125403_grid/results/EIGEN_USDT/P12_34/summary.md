# EMA Hourly Continuation — EIGEN/USDT P12_34

**Symbol:** EIGEN/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 492 |
| net_profit_factor | 0.8301 |
| net_win_rate | 0.5102 |
| gross_profit_factor | 1.0232 |
| gross_win_rate | 0.5102 |
| sharpe_ratio | -1.3408 |
| sortino_ratio | -0.4726 |
| max_drawdown | 0.4200 |
| cagr | -0.1978 |
| net_avg_win | 70.7912 |
| net_avg_loss | -88.8207 |
| avg_hold_time_bars | 6.2480 |
| exposure | 0.1711 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
