# EMA Hourly Continuation — MAGIC/USDT P20_26

**Symbol:** MAGIC/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1154 |
| net_profit_factor | 0.3688 |
| net_win_rate | 0.4151 |
| gross_profit_factor | 0.9773 |
| gross_win_rate | 0.4671 |
| sharpe_ratio | -10.9878 |
| sortino_ratio | -5.3298 |
| max_drawdown | 0.9989 |
| cagr | -0.9327 |
| net_avg_win | 12.1822 |
| net_avg_loss | -23.4428 |
| avg_hold_time_bars | 2.6040 |
| exposure | 0.1366 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
