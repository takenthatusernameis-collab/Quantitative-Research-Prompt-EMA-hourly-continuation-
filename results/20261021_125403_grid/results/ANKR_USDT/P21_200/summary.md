# EMA Hourly Continuation — ANKR/USDT P21_200

**Symbol:** ANKR/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 297 |
| net_profit_factor | 0.7849 |
| net_win_rate | 0.4949 |
| gross_profit_factor | 0.9883 |
| gross_win_rate | 0.4949 |
| sharpe_ratio | -1.3703 |
| sortino_ratio | -0.3373 |
| max_drawdown | 0.3755 |
| cagr | -0.1453 |
| net_avg_win | 80.8497 |
| net_avg_loss | -100.9523 |
| avg_hold_time_bars | 50.3502 |
| exposure | 0.6797 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
