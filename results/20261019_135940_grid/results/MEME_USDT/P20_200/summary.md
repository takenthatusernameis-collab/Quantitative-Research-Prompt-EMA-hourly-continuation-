# EMA Hourly Continuation — MEME/USDT P20_200

**Symbol:** MEME/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 373 |
| net_profit_factor | 0.8150 |
| net_win_rate | 0.5094 |
| gross_profit_factor | 1.0903 |
| gross_win_rate | 0.5228 |
| sharpe_ratio | -1.2404 |
| sortino_ratio | -0.3411 |
| max_drawdown | 0.3805 |
| cagr | -0.1483 |
| net_avg_win | 76.9320 |
| net_avg_loss | -97.9999 |
| avg_hold_time_bars | 38.7426 |
| exposure | 0.6569 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
