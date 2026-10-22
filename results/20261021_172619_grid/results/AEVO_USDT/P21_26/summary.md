# EMA Hourly Continuation — AEVO/USDT P21_26

**Symbol:** AEVO/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 264 |
| net_profit_factor | 0.5047 |
| net_win_rate | 0.4205 |
| gross_profit_factor | 0.7202 |
| gross_win_rate | 0.4205 |
| sharpe_ratio | -3.4710 |
| sortino_ratio | -0.8019 |
| max_drawdown | 0.6172 |
| cagr | -0.3092 |
| net_avg_win | 55.7015 |
| net_avg_loss | -80.0648 |
| avg_hold_time_bars | 4.8409 |
| exposure | 0.0578 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
