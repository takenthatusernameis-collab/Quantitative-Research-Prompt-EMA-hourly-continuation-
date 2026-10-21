# EMA Hourly Continuation — MANTA/USDT P20_55

**Symbol:** MANTA/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 541 |
| net_profit_factor | 0.6828 |
| net_win_rate | 0.4677 |
| gross_profit_factor | 0.8762 |
| gross_win_rate | 0.4677 |
| sharpe_ratio | -2.8465 |
| sortino_ratio | -0.9432 |
| max_drawdown | 0.6690 |
| cagr | -0.3513 |
| net_avg_win | 56.3853 |
| net_avg_loss | -72.5452 |
| avg_hold_time_bars | 9.2791 |
| exposure | 0.2282 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
