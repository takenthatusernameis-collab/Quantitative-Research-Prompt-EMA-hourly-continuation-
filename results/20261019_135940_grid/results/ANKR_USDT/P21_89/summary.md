# EMA Hourly Continuation — ANKR/USDT P21_89

**Symbol:** ANKR/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 699 |
| net_profit_factor | 0.5272 |
| net_win_rate | 0.4306 |
| gross_profit_factor | 0.8608 |
| gross_win_rate | 0.4464 |
| sharpe_ratio | -5.9266 |
| sortino_ratio | -2.1916 |
| max_drawdown | 0.9348 |
| cagr | -0.6587 |
| net_avg_win | 34.5606 |
| net_avg_loss | -49.5737 |
| avg_hold_time_bars | 13.4835 |
| exposure | 0.4284 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
