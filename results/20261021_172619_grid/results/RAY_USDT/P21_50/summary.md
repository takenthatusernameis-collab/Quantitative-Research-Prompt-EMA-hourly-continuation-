# EMA Hourly Continuation — RAY/USDT P21_50

**Symbol:** RAY/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 497 |
| net_profit_factor | 0.7587 |
| net_win_rate | 0.4909 |
| gross_profit_factor | 0.9876 |
| gross_win_rate | 0.4909 |
| sharpe_ratio | -2.1841 |
| sortino_ratio | -0.6960 |
| max_drawdown | 0.6248 |
| cagr | -0.2745 |
| net_avg_win | 71.3179 |
| net_avg_loss | -90.6526 |
| avg_hold_time_bars | 7.6559 |
| exposure | 0.1730 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
