# EMA Hourly Continuation — CTSI/USDT P21_144

**Symbol:** CTSI/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 436 |
| net_profit_factor | 0.7283 |
| net_win_rate | 0.4610 |
| gross_profit_factor | 0.8997 |
| gross_win_rate | 0.4610 |
| sharpe_ratio | -2.4541 |
| sortino_ratio | -0.7271 |
| max_drawdown | 0.6204 |
| cagr | -0.2855 |
| net_avg_win | 76.0441 |
| net_avg_loss | -89.3035 |
| avg_hold_time_bars | 26.3165 |
| exposure | 0.5215 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
