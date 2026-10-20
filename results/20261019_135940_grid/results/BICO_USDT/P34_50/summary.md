# EMA Hourly Continuation — BICO/USDT P34_50

**Symbol:** BICO/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 866 |
| net_profit_factor | 0.3649 |
| net_win_rate | 0.4411 |
| gross_profit_factor | 0.7480 |
| gross_win_rate | 0.4607 |
| sharpe_ratio | -7.2394 |
| sortino_ratio | -3.0289 |
| max_drawdown | 0.9739 |
| cagr | -0.7653 |
| net_avg_win | 14.6466 |
| net_avg_loss | -31.6786 |
| avg_hold_time_bars | 3.6928 |
| exposure | 0.1454 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
