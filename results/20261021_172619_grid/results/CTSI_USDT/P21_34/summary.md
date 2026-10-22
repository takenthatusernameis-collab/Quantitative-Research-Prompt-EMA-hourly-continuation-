# EMA Hourly Continuation — CTSI/USDT P21_34

**Symbol:** CTSI/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 462 |
| net_profit_factor | 0.5473 |
| net_win_rate | 0.4351 |
| gross_profit_factor | 0.8075 |
| gross_win_rate | 0.4351 |
| sharpe_ratio | -4.3874 |
| sortino_ratio | -1.3485 |
| max_drawdown | 0.7913 |
| cagr | -0.4620 |
| net_avg_win | 47.4692 |
| net_avg_loss | -66.7922 |
| avg_hold_time_bars | 5.8160 |
| exposure | 0.1221 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
