# EMA Hourly Continuation — MEME/USDT P55_200

**Symbol:** MEME/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 348 |
| net_profit_factor | 0.6855 |
| net_win_rate | 0.4856 |
| gross_profit_factor | 0.9565 |
| gross_win_rate | 0.4885 |
| sharpe_ratio | -2.2584 |
| sortino_ratio | -0.5881 |
| max_drawdown | 0.5187 |
| cagr | -0.2479 |
| net_avg_win | 65.8995 |
| net_avg_loss | -90.7656 |
| avg_hold_time_bars | 27.6609 |
| exposure | 0.4375 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
