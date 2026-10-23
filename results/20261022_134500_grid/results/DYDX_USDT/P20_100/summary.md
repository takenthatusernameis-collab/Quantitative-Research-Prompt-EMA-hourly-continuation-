# EMA Hourly Continuation — DYDX/USDT P20_100

**Symbol:** DYDX/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 633 |
| net_profit_factor | 0.6968 |
| net_win_rate | 0.4976 |
| gross_profit_factor | 1.0125 |
| gross_win_rate | 0.5039 |
| sharpe_ratio | -2.8029 |
| sortino_ratio | -1.0011 |
| max_drawdown | 0.6964 |
| cagr | -0.3730 |
| net_avg_win | 50.3722 |
| net_avg_loss | -71.6070 |
| avg_hold_time_bars | 15.9384 |
| exposure | 0.4586 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
