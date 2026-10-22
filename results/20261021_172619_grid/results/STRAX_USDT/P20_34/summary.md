# EMA Hourly Continuation — STRAX/USDT P20_34

**Symbol:** STRAX/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 535 |
| net_profit_factor | 0.5068 |
| net_win_rate | 0.4411 |
| gross_profit_factor | 0.7802 |
| gross_win_rate | 0.4430 |
| sharpe_ratio | -4.8612 |
| sortino_ratio | -1.6093 |
| max_drawdown | 0.8437 |
| cagr | -0.5243 |
| net_avg_win | 36.7244 |
| net_avg_loss | -57.1997 |
| avg_hold_time_bars | 6.9084 |
| exposure | 0.1690 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
