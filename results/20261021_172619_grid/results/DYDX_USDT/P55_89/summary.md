# EMA Hourly Continuation — DYDX/USDT P55_89

**Symbol:** DYDX/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 320 |
| net_profit_factor | 0.6790 |
| net_win_rate | 0.4844 |
| gross_profit_factor | 0.9158 |
| gross_win_rate | 0.4844 |
| sharpe_ratio | -1.9886 |
| sortino_ratio | -0.5092 |
| max_drawdown | 0.4476 |
| cagr | -0.2075 |
| net_avg_win | 60.3768 |
| net_avg_loss | -83.5300 |
| avg_hold_time_bars | 6.2281 |
| exposure | 0.0906 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
