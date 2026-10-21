# EMA Hourly Continuation — POKT/USDT P12_26

**Symbol:** POKT/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 549 |
| net_profit_factor | 0.5558 |
| net_win_rate | 0.3971 |
| gross_profit_factor | 0.7545 |
| gross_win_rate | 0.3971 |
| sharpe_ratio | -5.2694 |
| sortino_ratio | -1.7436 |
| max_drawdown | 0.8733 |
| cagr | -0.5550 |
| net_avg_win | 49.9453 |
| net_avg_loss | -59.1864 |
| avg_hold_time_bars | 5.9545 |
| exposure | 0.1479 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
