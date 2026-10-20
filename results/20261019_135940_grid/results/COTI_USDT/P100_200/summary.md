# EMA Hourly Continuation — COTI/USDT P100_200

**Symbol:** COTI/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 393 |
| net_profit_factor | 0.7455 |
| net_win_rate | 0.5267 |
| gross_profit_factor | 1.1061 |
| gross_win_rate | 0.5267 |
| sharpe_ratio | -1.8089 |
| sortino_ratio | -0.5121 |
| max_drawdown | 0.4814 |
| cagr | -0.2133 |
| net_avg_win | 64.0318 |
| net_avg_loss | -95.5943 |
| avg_hold_time_bars | 8.7608 |
| exposure | 0.1565 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
