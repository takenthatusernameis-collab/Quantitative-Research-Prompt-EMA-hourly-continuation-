# EMA Hourly Continuation — DYDX/USDT P89_200

**Symbol:** DYDX/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 283 |
| net_profit_factor | 0.8025 |
| net_win_rate | 0.4982 |
| gross_profit_factor | 0.9915 |
| gross_win_rate | 0.4982 |
| sharpe_ratio | -1.1528 |
| sortino_ratio | -0.2777 |
| max_drawdown | 0.3149 |
| cagr | -0.1206 |
| net_avg_win | 79.4802 |
| net_avg_loss | -98.3417 |
| avg_hold_time_bars | 14.0742 |
| exposure | 0.1810 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
