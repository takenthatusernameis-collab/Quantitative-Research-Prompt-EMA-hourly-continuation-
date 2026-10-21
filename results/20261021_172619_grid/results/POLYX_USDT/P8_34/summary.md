# EMA Hourly Continuation — POLYX/USDT P8_34

**Symbol:** POLYX/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 835 |
| net_profit_factor | 0.7392 |
| net_win_rate | 0.4946 |
| gross_profit_factor | 1.0135 |
| gross_win_rate | 0.4958 |
| sharpe_ratio | -3.2765 |
| sortino_ratio | -1.3561 |
| max_drawdown | 0.8090 |
| cagr | -0.4620 |
| net_avg_win | 54.1512 |
| net_avg_loss | -71.6973 |
| avg_hold_time_bars | 8.0946 |
| exposure | 0.3072 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
