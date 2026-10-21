# EMA Hourly Continuation — GALA/USDT P26_200

**Symbol:** GALA/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 287 |
| net_profit_factor | 0.8337 |
| net_win_rate | 0.4983 |
| gross_profit_factor | 0.9763 |
| gross_win_rate | 0.4983 |
| sharpe_ratio | -0.8421 |
| sortino_ratio | -0.2040 |
| max_drawdown | 0.3134 |
| cagr | -0.0915 |
| net_avg_win | 75.0643 |
| net_avg_loss | -89.4105 |
| avg_hold_time_bars | 43.9199 |
| exposure | 0.5730 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
