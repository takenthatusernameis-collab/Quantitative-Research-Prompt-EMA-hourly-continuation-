# EMA Hourly Continuation — DYDX/USDT P26_50

**Symbol:** DYDX/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 975 |
| net_profit_factor | 0.4917 |
| net_win_rate | 0.4492 |
| gross_profit_factor | 0.9141 |
| gross_win_rate | 0.4656 |
| sharpe_ratio | -7.5023 |
| sortino_ratio | -3.3042 |
| max_drawdown | 0.9836 |
| cagr | -0.8018 |
| net_avg_win | 21.7074 |
| net_avg_loss | -36.0076 |
| avg_hold_time_bars | 3.7221 |
| exposure | 0.1650 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
