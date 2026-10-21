# EMA Hourly Continuation — RAY/USDT P8_100

**Symbol:** RAY/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 508 |
| net_profit_factor | 0.9163 |
| net_win_rate | 0.5197 |
| gross_profit_factor | 1.0729 |
| gross_win_rate | 0.5197 |
| sharpe_ratio | -0.5559 |
| sortino_ratio | -0.1802 |
| max_drawdown | 0.3251 |
| cagr | -0.0854 |
| net_avg_win | 83.3548 |
| net_avg_loss | -98.4204 |
| avg_hold_time_bars | 27.0610 |
| exposure | 0.6249 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
