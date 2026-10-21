# EMA Hourly Continuation — PEPE/USDT P50_100

**Symbol:** PEPE/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 313 |
| net_profit_factor | 0.8529 |
| net_win_rate | 0.5208 |
| gross_profit_factor | 1.0762 |
| gross_win_rate | 0.5208 |
| sharpe_ratio | -0.8341 |
| sortino_ratio | -0.2125 |
| max_drawdown | 0.2476 |
| cagr | -0.0946 |
| net_avg_win | 78.5449 |
| net_avg_loss | -100.0738 |
| avg_hold_time_bars | 9.4856 |
| exposure | 0.1350 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
