# EMA Hourly Continuation — DEXE/USDT P50_55

**Symbol:** DEXE/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 808 |
| net_profit_factor | 0.2040 |
| net_win_rate | 0.3243 |
| gross_profit_factor | 0.6290 |
| gross_win_rate | 0.3787 |
| sharpe_ratio | -12.7309 |
| sortino_ratio | -5.3305 |
| max_drawdown | 0.9993 |
| cagr | -0.9430 |
| net_avg_win | 9.7764 |
| net_avg_loss | -22.9925 |
| avg_hold_time_bars | 4.2847 |
| exposure | 0.1574 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
