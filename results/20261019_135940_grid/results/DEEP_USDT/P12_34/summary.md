# EMA Hourly Continuation — DEEP/USDT P12_34

**Symbol:** DEEP/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 978 |
| net_profit_factor | 0.6252 |
| net_win_rate | 0.4560 |
| gross_profit_factor | 0.9156 |
| gross_win_rate | 0.4683 |
| sharpe_ratio | -6.5430 |
| sortino_ratio | -3.2158 |
| max_drawdown | 0.9576 |
| cagr | -0.7881 |
| net_avg_win | 35.7626 |
| net_avg_loss | -47.9549 |
| avg_hold_time_bars | 4.1319 |
| exposure | 0.2288 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
