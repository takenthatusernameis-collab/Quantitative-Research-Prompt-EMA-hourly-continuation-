# EMA Hourly Continuation — DYDX/USDT P50_200

**Symbol:** DYDX/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 373 |
| net_profit_factor | 0.8425 |
| net_win_rate | 0.5335 |
| gross_profit_factor | 1.1277 |
| gross_win_rate | 0.5335 |
| sharpe_ratio | -0.9243 |
| sortino_ratio | -0.2560 |
| max_drawdown | 0.3370 |
| cagr | -0.1139 |
| net_avg_win | 70.3768 |
| net_avg_loss | -95.5390 |
| avg_hold_time_bars | 24.8981 |
| exposure | 0.4221 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
