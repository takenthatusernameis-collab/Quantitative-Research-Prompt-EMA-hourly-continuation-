# EMA Hourly Continuation — FLIP/USDT P20_200

**Symbol:** FLIP/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 304 |
| net_profit_factor | 0.6364 |
| net_win_rate | 0.4638 |
| gross_profit_factor | 0.8675 |
| gross_win_rate | 0.4704 |
| sharpe_ratio | -2.3316 |
| sortino_ratio | -0.5709 |
| max_drawdown | 0.5127 |
| cagr | -0.2369 |
| net_avg_win | 61.1906 |
| net_avg_loss | -83.1712 |
| avg_hold_time_bars | 44.6908 |
| exposure | 0.6175 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
