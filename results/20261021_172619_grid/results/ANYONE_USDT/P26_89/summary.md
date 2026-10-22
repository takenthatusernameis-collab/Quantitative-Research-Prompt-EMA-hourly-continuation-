# EMA Hourly Continuation — ANYONE/USDT P26_89

**Symbol:** ANYONE/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 413 |
| net_profit_factor | 0.7262 |
| net_win_rate | 0.4600 |
| gross_profit_factor | 0.8462 |
| gross_win_rate | 0.4600 |
| sharpe_ratio | -2.1493 |
| sortino_ratio | -0.6530 |
| max_drawdown | 0.5229 |
| cagr | -0.2605 |
| net_avg_win | 68.9887 |
| net_avg_loss | -80.9422 |
| avg_hold_time_bars | 14.2470 |
| exposure | 0.2973 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
