# EMA Hourly Continuation — MEME/USDT P26_200

**Symbol:** MEME/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 349 |
| net_profit_factor | 0.8019 |
| net_win_rate | 0.5072 |
| gross_profit_factor | 1.1090 |
| gross_win_rate | 0.5272 |
| sharpe_ratio | -1.2789 |
| sortino_ratio | -0.3385 |
| max_drawdown | 0.4103 |
| cagr | -0.1481 |
| net_avg_win | 75.8172 |
| net_avg_loss | -97.2897 |
| avg_hold_time_bars | 39.4585 |
| exposure | 0.6260 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
