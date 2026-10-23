# EMA Hourly Continuation — SAFE/USDT P20_50

**Symbol:** SAFE/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 953 |
| net_profit_factor | 0.5312 |
| net_win_rate | 0.4732 |
| gross_profit_factor | 0.9325 |
| gross_win_rate | 0.4827 |
| sharpe_ratio | -5.8647 |
| sortino_ratio | -2.5584 |
| max_drawdown | 0.9548 |
| cagr | -0.7077 |
| net_avg_win | 23.9494 |
| net_avg_loss | -40.5083 |
| avg_hold_time_bars | 5.4292 |
| exposure | 0.2369 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
