# EMA Hourly Continuation — MEME/USDT P100_144

**Symbol:** MEME/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 533 |
| net_profit_factor | 0.5329 |
| net_win_rate | 0.4765 |
| gross_profit_factor | 0.9215 |
| gross_win_rate | 0.4859 |
| sharpe_ratio | -4.5515 |
| sortino_ratio | -1.4721 |
| max_drawdown | 0.8444 |
| cagr | -0.5188 |
| net_avg_win | 37.7637 |
| net_avg_loss | -64.5113 |
| avg_hold_time_bars | 4.5647 |
| exposure | 0.1106 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
