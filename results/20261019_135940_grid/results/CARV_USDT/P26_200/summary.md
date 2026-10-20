# EMA Hourly Continuation — CARV/USDT P26_200

**Symbol:** CARV/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 339 |
| net_profit_factor | 0.5986 |
| net_win_rate | 0.4484 |
| gross_profit_factor | 0.8468 |
| gross_win_rate | 0.4572 |
| sharpe_ratio | -3.2785 |
| sortino_ratio | -0.9471 |
| max_drawdown | 0.6213 |
| cagr | -0.3571 |
| net_avg_win | 58.0677 |
| net_avg_loss | -78.8482 |
| avg_hold_time_bars | 27.0295 |
| exposure | 0.5156 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
