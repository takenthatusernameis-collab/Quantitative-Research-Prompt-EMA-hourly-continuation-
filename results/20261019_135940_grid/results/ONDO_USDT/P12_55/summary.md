# EMA Hourly Continuation — ONDO/USDT P12_55

**Symbol:** ONDO/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1031 |
| net_profit_factor | 0.6359 |
| net_win_rate | 0.4724 |
| gross_profit_factor | 0.9610 |
| gross_win_rate | 0.4811 |
| sharpe_ratio | -5.4215 |
| sortino_ratio | -2.4495 |
| max_drawdown | 0.9491 |
| cagr | -0.6910 |
| net_avg_win | 33.9782 |
| net_avg_loss | -47.8372 |
| avg_hold_time_bars | 7.3676 |
| exposure | 0.3453 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
