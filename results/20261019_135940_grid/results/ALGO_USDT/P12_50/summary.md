# EMA Hourly Continuation — ALGO/USDT P12_50

**Symbol:** ALGO/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1046 |
| net_profit_factor | 0.5535 |
| net_win_rate | 0.4885 |
| gross_profit_factor | 0.9428 |
| gross_win_rate | 0.4971 |
| sharpe_ratio | -5.6504 |
| sortino_ratio | -2.5636 |
| max_drawdown | 0.9588 |
| cagr | -0.7129 |
| net_avg_win | 23.2002 |
| net_avg_loss | -40.0373 |
| avg_hold_time_bars | 7.4541 |
| exposure | 0.3544 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
