# EMA Hourly Continuation — PROM/USDT P21_55

**Symbol:** PROM/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 993 |
| net_profit_factor | 0.4309 |
| net_win_rate | 0.4079 |
| gross_profit_factor | 0.8285 |
| gross_win_rate | 0.4391 |
| sharpe_ratio | -8.9306 |
| sortino_ratio | -3.9626 |
| max_drawdown | 0.9931 |
| cagr | -0.8622 |
| net_avg_win | 18.5636 |
| net_avg_loss | -29.6757 |
| avg_hold_time_bars | 5.4099 |
| exposure | 0.2442 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
