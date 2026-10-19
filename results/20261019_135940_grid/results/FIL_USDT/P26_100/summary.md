# EMA Hourly Continuation — FIL/USDT P26_100

**Symbol:** FIL/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 656 |
| net_profit_factor | 0.5144 |
| net_win_rate | 0.4405 |
| gross_profit_factor | 0.8270 |
| gross_win_rate | 0.4436 |
| sharpe_ratio | -5.4291 |
| sortino_ratio | -1.9511 |
| max_drawdown | 0.9123 |
| cagr | -0.6113 |
| net_avg_win | 33.2404 |
| net_avg_loss | -50.8843 |
| avg_hold_time_bars | 11.3049 |
| exposure | 0.3371 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
