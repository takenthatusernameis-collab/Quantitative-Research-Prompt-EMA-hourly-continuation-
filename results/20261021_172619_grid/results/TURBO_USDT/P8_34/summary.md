# EMA Hourly Continuation — TURBO/USDT P8_34

**Symbol:** TURBO/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 599 |
| net_profit_factor | 0.8249 |
| net_win_rate | 0.5092 |
| gross_profit_factor | 1.0289 |
| gross_win_rate | 0.5092 |
| sharpe_ratio | -1.6542 |
| sortino_ratio | -0.6368 |
| max_drawdown | 0.5072 |
| cagr | -0.2557 |
| net_avg_win | 71.2162 |
| net_avg_loss | -89.5605 |
| avg_hold_time_bars | 8.9466 |
| exposure | 0.2923 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
