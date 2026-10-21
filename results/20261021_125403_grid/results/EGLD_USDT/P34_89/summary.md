# EMA Hourly Continuation — EGLD/USDT P34_89

**Symbol:** EGLD/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 430 |
| net_profit_factor | 0.7967 |
| net_win_rate | 0.5186 |
| gross_profit_factor | 1.0702 |
| gross_win_rate | 0.5186 |
| sharpe_ratio | -1.4384 |
| sortino_ratio | -0.4296 |
| max_drawdown | 0.4218 |
| cagr | -0.1795 |
| net_avg_win | 68.7791 |
| net_avg_loss | -93.0064 |
| avg_hold_time_bars | 12.1256 |
| exposure | 0.2370 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
