# EMA Hourly Continuation — WEMIX/USDT P50_55

**Symbol:** WEMIX/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1267 |
| net_profit_factor | 0.0585 |
| net_win_rate | 0.1902 |
| gross_profit_factor | 0.2678 |
| gross_win_rate | 0.2502 |
| sharpe_ratio | -21.5382 |
| sortino_ratio | -12.0370 |
| max_drawdown | 1.0000 |
| cagr | -0.9987 |
| net_avg_win | 2.5791 |
| net_avg_loss | -10.3524 |
| avg_hold_time_bars | 1.9826 |
| exposure | 0.1142 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
