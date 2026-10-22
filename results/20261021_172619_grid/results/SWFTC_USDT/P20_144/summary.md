# EMA Hourly Continuation — SWFTC/USDT P20_144

**Symbol:** SWFTC/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 383 |
| net_profit_factor | 0.7281 |
| net_win_rate | 0.4674 |
| gross_profit_factor | 0.8886 |
| gross_win_rate | 0.4674 |
| sharpe_ratio | -2.0837 |
| sortino_ratio | -0.5790 |
| max_drawdown | 0.4930 |
| cagr | -0.2342 |
| net_avg_win | 73.0385 |
| net_avg_loss | -88.0244 |
| avg_hold_time_bars | 26.7728 |
| exposure | 0.4661 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
