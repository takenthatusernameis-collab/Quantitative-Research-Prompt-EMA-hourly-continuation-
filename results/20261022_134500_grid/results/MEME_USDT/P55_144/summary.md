# EMA Hourly Continuation — MEME/USDT P55_144

**Symbol:** MEME/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 479 |
| net_profit_factor | 0.5884 |
| net_win_rate | 0.4551 |
| gross_profit_factor | 0.8551 |
| gross_win_rate | 0.4614 |
| sharpe_ratio | -3.8049 |
| sortino_ratio | -1.1703 |
| max_drawdown | 0.7623 |
| cagr | -0.4306 |
| net_avg_win | 49.6281 |
| net_avg_loss | -70.4525 |
| avg_hold_time_bars | 13.6409 |
| exposure | 0.2970 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
