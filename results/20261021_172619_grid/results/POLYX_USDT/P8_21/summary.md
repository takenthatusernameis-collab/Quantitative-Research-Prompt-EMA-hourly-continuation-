# EMA Hourly Continuation — POLYX/USDT P8_21

**Symbol:** POLYX/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 721 |
| net_profit_factor | 0.7044 |
| net_win_rate | 0.4938 |
| gross_profit_factor | 1.0465 |
| gross_win_rate | 0.4938 |
| sharpe_ratio | -3.7532 |
| sortino_ratio | -1.4474 |
| max_drawdown | 0.8195 |
| cagr | -0.4838 |
| net_avg_win | 54.2132 |
| net_avg_loss | -75.0675 |
| avg_hold_time_bars | 5.5603 |
| exposure | 0.1822 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
