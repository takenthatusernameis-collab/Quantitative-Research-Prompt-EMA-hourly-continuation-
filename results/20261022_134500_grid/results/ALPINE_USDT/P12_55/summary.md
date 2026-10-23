# EMA Hourly Continuation — ALPINE/USDT P12_55

**Symbol:** ALPINE/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 940 |
| net_profit_factor | 0.4675 |
| net_win_rate | 0.4170 |
| gross_profit_factor | 0.7760 |
| gross_win_rate | 0.4383 |
| sharpe_ratio | -7.5612 |
| sortino_ratio | -3.2599 |
| max_drawdown | 0.9823 |
| cagr | -0.7974 |
| net_avg_win | 21.9935 |
| net_avg_loss | -33.6496 |
| avg_hold_time_bars | 8.6851 |
| exposure | 0.3711 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
