# EMA Hourly Continuation — OSMO/USDT P34_55

**Symbol:** OSMO/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 874 |
| net_profit_factor | 0.3518 |
| net_win_rate | 0.3902 |
| gross_profit_factor | 0.8045 |
| gross_win_rate | 0.4245 |
| sharpe_ratio | -9.5616 |
| sortino_ratio | -4.0334 |
| max_drawdown | 0.9936 |
| cagr | -0.8657 |
| net_avg_win | 15.8102 |
| net_avg_loss | -28.7556 |
| avg_hold_time_bars | 3.8009 |
| exposure | 0.1510 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
