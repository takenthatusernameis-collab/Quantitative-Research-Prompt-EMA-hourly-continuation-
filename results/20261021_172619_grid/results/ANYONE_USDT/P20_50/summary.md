# EMA Hourly Continuation — ANYONE/USDT P20_50

**Symbol:** ANYONE/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 474 |
| net_profit_factor | 0.6102 |
| net_win_rate | 0.4304 |
| gross_profit_factor | 0.7363 |
| gross_win_rate | 0.4304 |
| sharpe_ratio | -3.4748 |
| sortino_ratio | -1.1260 |
| max_drawdown | 0.7012 |
| cagr | -0.4058 |
| net_avg_win | 53.0495 |
| net_avg_loss | -65.6904 |
| avg_hold_time_bars | 7.4283 |
| exposure | 0.1779 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
