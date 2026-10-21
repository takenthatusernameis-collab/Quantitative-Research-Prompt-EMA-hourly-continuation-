# EMA Hourly Continuation — CSPR/USDT P21_55

**Symbol:** CSPR/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 486 |
| net_profit_factor | 0.6876 |
| net_win_rate | 0.4691 |
| gross_profit_factor | 0.8907 |
| gross_win_rate | 0.4691 |
| sharpe_ratio | -2.6361 |
| sortino_ratio | -0.8284 |
| max_drawdown | 0.6193 |
| cagr | -0.3160 |
| net_avg_win | 59.3360 |
| net_avg_loss | -76.2606 |
| avg_hold_time_bars | 7.2593 |
| exposure | 0.1604 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
