# EMA Hourly Continuation — MEME/USDT P34_200

**Symbol:** MEME/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 358 |
| net_profit_factor | 0.8280 |
| net_win_rate | 0.5168 |
| gross_profit_factor | 1.1004 |
| gross_win_rate | 0.5251 |
| sharpe_ratio | -1.0975 |
| sortino_ratio | -0.2962 |
| max_drawdown | 0.3467 |
| cagr | -0.1303 |
| net_avg_win | 76.9596 |
| net_avg_loss | -99.3889 |
| avg_hold_time_bars | 33.2989 |
| exposure | 0.5419 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
