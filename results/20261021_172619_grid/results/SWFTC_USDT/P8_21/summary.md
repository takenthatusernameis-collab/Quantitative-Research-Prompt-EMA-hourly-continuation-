# EMA Hourly Continuation — SWFTC/USDT P8_21

**Symbol:** SWFTC/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 474 |
| net_profit_factor | 0.7982 |
| net_win_rate | 0.5190 |
| gross_profit_factor | 1.0888 |
| gross_win_rate | 0.5190 |
| sharpe_ratio | -1.6054 |
| sortino_ratio | -0.5035 |
| max_drawdown | 0.4770 |
| cagr | -0.2063 |
| net_avg_win | 70.7717 |
| net_avg_loss | -95.6656 |
| avg_hold_time_bars | 6.2468 |
| exposure | 0.1346 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
