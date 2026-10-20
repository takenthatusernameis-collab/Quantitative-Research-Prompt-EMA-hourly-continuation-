# EMA Hourly Continuation — PHA/USDT P55_200

**Symbol:** PHA/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 437 |
| net_profit_factor | 0.5934 |
| net_win_rate | 0.4508 |
| gross_profit_factor | 0.8302 |
| gross_win_rate | 0.4554 |
| sharpe_ratio | -3.2338 |
| sortino_ratio | -0.9517 |
| max_drawdown | 0.6808 |
| cagr | -0.3614 |
| net_avg_win | 50.0634 |
| net_avg_loss | -69.2507 |
| avg_hold_time_bars | 16.6819 |
| exposure | 0.3314 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
