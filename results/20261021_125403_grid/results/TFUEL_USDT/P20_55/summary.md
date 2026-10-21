# EMA Hourly Continuation — TFUEL/USDT P20_55

**Symbol:** TFUEL/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 578 |
| net_profit_factor | 0.5619 |
| net_win_rate | 0.4187 |
| gross_profit_factor | 0.7842 |
| gross_win_rate | 0.4187 |
| sharpe_ratio | -5.0784 |
| sortino_ratio | -1.7329 |
| max_drawdown | 0.8695 |
| cagr | -0.5508 |
| net_avg_win | 45.9652 |
| net_avg_loss | -58.9152 |
| avg_hold_time_bars | 8.3806 |
| exposure | 0.2192 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
