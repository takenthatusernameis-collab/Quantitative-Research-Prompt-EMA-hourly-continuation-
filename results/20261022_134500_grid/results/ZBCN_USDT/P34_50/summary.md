# EMA Hourly Continuation — ZBCN/USDT P34_50

**Symbol:** ZBCN/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 968 |
| net_profit_factor | 0.4267 |
| net_win_rate | 0.4267 |
| gross_profit_factor | 0.8463 |
| gross_win_rate | 0.4329 |
| sharpe_ratio | -9.0125 |
| sortino_ratio | -3.9734 |
| max_drawdown | 0.9937 |
| cagr | -0.8713 |
| net_avg_win | 17.9078 |
| net_avg_loss | -31.2295 |
| avg_hold_time_bars | 2.2366 |
| exposure | 0.1002 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
