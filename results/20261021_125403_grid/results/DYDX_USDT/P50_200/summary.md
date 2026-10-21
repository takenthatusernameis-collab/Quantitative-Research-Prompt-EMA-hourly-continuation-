# EMA Hourly Continuation — DYDX/USDT P50_200

**Symbol:** DYDX/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 293 |
| net_profit_factor | 0.9088 |
| net_win_rate | 0.5256 |
| gross_profit_factor | 1.0924 |
| gross_win_rate | 0.5256 |
| sharpe_ratio | -0.4366 |
| sortino_ratio | -0.1077 |
| max_drawdown | 0.2556 |
| cagr | -0.0517 |
| net_avg_win | 80.6761 |
| net_avg_loss | -98.3531 |
| avg_hold_time_bars | 31.1229 |
| exposure | 0.4145 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
