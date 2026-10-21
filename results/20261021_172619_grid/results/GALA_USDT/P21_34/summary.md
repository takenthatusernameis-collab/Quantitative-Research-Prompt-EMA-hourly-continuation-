# EMA Hourly Continuation — GALA/USDT P21_34

**Symbol:** GALA/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 303 |
| net_profit_factor | 0.6580 |
| net_win_rate | 0.4686 |
| gross_profit_factor | 0.9078 |
| gross_win_rate | 0.4686 |
| sharpe_ratio | -2.4551 |
| sortino_ratio | -0.6111 |
| max_drawdown | 0.5193 |
| cagr | -0.2442 |
| net_avg_win | 68.4248 |
| net_avg_loss | -91.7129 |
| avg_hold_time_bars | 4.5413 |
| exposure | 0.0625 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
