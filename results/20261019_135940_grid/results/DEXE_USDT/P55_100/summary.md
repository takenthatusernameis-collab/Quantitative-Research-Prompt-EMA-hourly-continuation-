# EMA Hourly Continuation — DEXE/USDT P55_100

**Symbol:** DEXE/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 500 |
| net_profit_factor | 0.4932 |
| net_win_rate | 0.4700 |
| gross_profit_factor | 0.8064 |
| gross_win_rate | 0.4740 |
| sharpe_ratio | -4.0670 |
| sortino_ratio | -1.2881 |
| max_drawdown | 0.7982 |
| cagr | -0.4587 |
| net_avg_win | 32.5525 |
| net_avg_loss | -58.5256 |
| avg_hold_time_bars | 13.8300 |
| exposure | 0.3143 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
