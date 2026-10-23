# EMA Hourly Continuation — PEOPLE/USDT P50_144

**Symbol:** PEOPLE/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 476 |
| net_profit_factor | 0.6791 |
| net_win_rate | 0.4790 |
| gross_profit_factor | 0.9243 |
| gross_win_rate | 0.4811 |
| sharpe_ratio | -2.7594 |
| sortino_ratio | -0.8477 |
| max_drawdown | 0.6712 |
| cagr | -0.3300 |
| net_avg_win | 59.0241 |
| net_avg_loss | -79.9032 |
| avg_hold_time_bars | 13.9958 |
| exposure | 0.3015 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
