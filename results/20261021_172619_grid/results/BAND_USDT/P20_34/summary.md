# EMA Hourly Continuation — BAND/USDT P20_34

**Symbol:** BAND/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 566 |
| net_profit_factor | 0.6778 |
| net_win_rate | 0.4982 |
| gross_profit_factor | 1.0380 |
| gross_win_rate | 0.5018 |
| sharpe_ratio | -3.2685 |
| sortino_ratio | -1.1168 |
| max_drawdown | 0.7404 |
| cagr | -0.3989 |
| net_avg_win | 53.9372 |
| net_avg_loss | -79.0177 |
| avg_hold_time_bars | 5.0972 |
| exposure | 0.1305 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
