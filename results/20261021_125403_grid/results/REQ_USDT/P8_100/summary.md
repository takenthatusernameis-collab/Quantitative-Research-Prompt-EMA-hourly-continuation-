# EMA Hourly Continuation — REQ/USDT P8_100

**Symbol:** REQ/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 591 |
| net_profit_factor | 0.5750 |
| net_win_rate | 0.4196 |
| gross_profit_factor | 0.7663 |
| gross_win_rate | 0.4196 |
| sharpe_ratio | -4.9015 |
| sortino_ratio | -1.6864 |
| max_drawdown | 0.8639 |
| cagr | -0.5451 |
| net_avg_win | 46.9986 |
| net_avg_loss | -59.1023 |
| avg_hold_time_bars | 21.3029 |
| exposure | 0.5723 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
