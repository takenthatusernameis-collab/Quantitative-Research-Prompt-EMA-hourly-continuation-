# EMA Hourly Continuation — DYDX/USDT P20_21

**Symbol:** DYDX/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1243 |
| net_profit_factor | 0.1487 |
| net_win_rate | 0.3250 |
| gross_profit_factor | 0.7730 |
| gross_win_rate | 0.3918 |
| sharpe_ratio | -16.9162 |
| sortino_ratio | -8.8892 |
| max_drawdown | 1.0000 |
| cagr | -0.9932 |
| net_avg_win | 4.3239 |
| net_avg_loss | -14.0010 |
| avg_hold_time_bars | 1.6854 |
| exposure | 0.0952 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
