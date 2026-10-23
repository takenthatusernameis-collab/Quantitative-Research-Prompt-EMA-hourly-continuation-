# EMA Hourly Continuation — PEOPLE/USDT P21_144

**Symbol:** PEOPLE/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 410 |
| net_profit_factor | 0.8733 |
| net_win_rate | 0.5341 |
| gross_profit_factor | 1.1724 |
| gross_win_rate | 0.5439 |
| sharpe_ratio | -0.7810 |
| sortino_ratio | -0.2263 |
| max_drawdown | 0.3549 |
| cagr | -0.1029 |
| net_avg_win | 75.4335 |
| net_avg_loss | -99.0411 |
| avg_hold_time_bars | 31.3707 |
| exposure | 0.5820 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
