# EMA Hourly Continuation — TRAC/USDT P34_200

**Symbol:** TRAC/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 408 |
| net_profit_factor | 0.6765 |
| net_win_rate | 0.4779 |
| gross_profit_factor | 0.9385 |
| gross_win_rate | 0.4853 |
| sharpe_ratio | -2.4909 |
| sortino_ratio | -0.7055 |
| max_drawdown | 0.5844 |
| cagr | -0.2850 |
| net_avg_win | 61.0461 |
| net_avg_loss | -82.6153 |
| avg_hold_time_bars | 25.6299 |
| exposure | 0.4753 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
