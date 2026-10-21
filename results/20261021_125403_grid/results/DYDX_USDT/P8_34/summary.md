# EMA Hourly Continuation — DYDX/USDT P8_34

**Symbol:** DYDX/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 710 |
| net_profit_factor | 0.7448 |
| net_win_rate | 0.4817 |
| gross_profit_factor | 0.9618 |
| gross_win_rate | 0.4817 |
| sharpe_ratio | -2.7628 |
| sortino_ratio | -1.0514 |
| max_drawdown | 0.7073 |
| cagr | -0.3825 |
| net_avg_win | 59.9214 |
| net_avg_loss | -74.7644 |
| avg_hold_time_bars | 10.1718 |
| exposure | 0.3283 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
