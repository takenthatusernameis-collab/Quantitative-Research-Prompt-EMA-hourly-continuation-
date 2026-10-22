# EMA Hourly Continuation — ATOM/USDT P21_200

**Symbol:** ATOM/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 375 |
| net_profit_factor | 0.7047 |
| net_win_rate | 0.5067 |
| gross_profit_factor | 1.0189 |
| gross_win_rate | 0.5093 |
| sharpe_ratio | -1.9746 |
| sortino_ratio | -0.5389 |
| max_drawdown | 0.5087 |
| cagr | -0.2268 |
| net_avg_win | 59.7624 |
| net_avg_loss | -87.1007 |
| avg_hold_time_bars | 35.6107 |
| exposure | 0.6070 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
