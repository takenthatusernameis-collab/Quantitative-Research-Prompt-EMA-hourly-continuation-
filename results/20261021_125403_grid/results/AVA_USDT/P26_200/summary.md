# EMA Hourly Continuation — AVA/USDT P26_200

**Symbol:** AVA/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 336 |
| net_profit_factor | 0.8463 |
| net_win_rate | 0.5089 |
| gross_profit_factor | 1.0146 |
| gross_win_rate | 0.5089 |
| sharpe_ratio | -0.8298 |
| sortino_ratio | -0.2183 |
| max_drawdown | 0.3355 |
| cagr | -0.0978 |
| net_avg_win | 73.2934 |
| net_avg_loss | -89.7576 |
| avg_hold_time_bars | 33.7411 |
| exposure | 0.5153 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
