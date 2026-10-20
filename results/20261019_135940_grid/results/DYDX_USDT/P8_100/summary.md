# EMA Hourly Continuation — DYDX/USDT P8_100

**Symbol:** DYDX/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 531 |
| net_profit_factor | 0.7232 |
| net_win_rate | 0.4953 |
| gross_profit_factor | 0.9987 |
| gross_win_rate | 0.4991 |
| sharpe_ratio | -2.4360 |
| sortino_ratio | -0.7957 |
| max_drawdown | 0.6266 |
| cagr | -0.3111 |
| net_avg_win | 60.3647 |
| net_avg_loss | -81.9172 |
| avg_hold_time_bars | 29.6384 |
| exposure | 0.7154 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
