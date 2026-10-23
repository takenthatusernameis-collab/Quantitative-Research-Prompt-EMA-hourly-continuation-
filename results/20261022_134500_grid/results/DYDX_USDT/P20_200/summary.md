# EMA Hourly Continuation — DYDX/USDT P20_200

**Symbol:** DYDX/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 380 |
| net_profit_factor | 0.7377 |
| net_win_rate | 0.5026 |
| gross_profit_factor | 1.0059 |
| gross_win_rate | 0.5053 |
| sharpe_ratio | -1.7403 |
| sortino_ratio | -0.4782 |
| max_drawdown | 0.4627 |
| cagr | -0.2041 |
| net_avg_win | 64.2423 |
| net_avg_loss | -88.0060 |
| avg_hold_time_bars | 38.0500 |
| exposure | 0.6572 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
