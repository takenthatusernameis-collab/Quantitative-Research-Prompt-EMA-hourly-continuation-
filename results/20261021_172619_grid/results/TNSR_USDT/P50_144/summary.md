# EMA Hourly Continuation — TNSR/USDT P50_144

**Symbol:** TNSR/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 381 |
| net_profit_factor | 0.7509 |
| net_win_rate | 0.4803 |
| gross_profit_factor | 0.9285 |
| gross_win_rate | 0.4803 |
| sharpe_ratio | -1.8427 |
| sortino_ratio | -0.5110 |
| max_drawdown | 0.4546 |
| cagr | -0.2106 |
| net_avg_win | 74.0046 |
| net_avg_loss | -91.0877 |
| avg_hold_time_bars | 16.1339 |
| exposure | 0.2782 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
