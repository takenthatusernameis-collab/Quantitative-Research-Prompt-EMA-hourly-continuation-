# EMA Hourly Continuation — FIDA/USDT P26_100

**Symbol:** FIDA/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 490 |
| net_profit_factor | 0.6907 |
| net_win_rate | 0.4796 |
| gross_profit_factor | 0.8911 |
| gross_win_rate | 0.4796 |
| sharpe_ratio | -2.3398 |
| sortino_ratio | -0.7367 |
| max_drawdown | 0.5927 |
| cagr | -0.2873 |
| net_avg_win | 54.5949 |
| net_avg_loss | -72.8419 |
| avg_hold_time_bars | 15.3020 |
| exposure | 0.3393 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
