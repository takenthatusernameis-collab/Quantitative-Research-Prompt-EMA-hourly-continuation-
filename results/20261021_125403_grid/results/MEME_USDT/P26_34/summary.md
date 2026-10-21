# EMA Hourly Continuation — MEME/USDT P26_34

**Symbol:** MEME/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 243 |
| net_profit_factor | 0.5713 |
| net_win_rate | 0.4362 |
| gross_profit_factor | 0.8146 |
| gross_win_rate | 0.4403 |
| sharpe_ratio | -2.9217 |
| sortino_ratio | -0.6503 |
| max_drawdown | 0.5280 |
| cagr | -0.2584 |
| net_avg_win | 66.3806 |
| net_avg_loss | -89.9034 |
| avg_hold_time_bars | 4.2428 |
| exposure | 0.0469 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
