# EMA Hourly Continuation — FIDA/USDT P89_144

**Symbol:** FIDA/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 516 |
| net_profit_factor | 0.4771 |
| net_win_rate | 0.4419 |
| gross_profit_factor | 0.8066 |
| gross_win_rate | 0.4496 |
| sharpe_ratio | -4.9956 |
| sortino_ratio | -1.6047 |
| max_drawdown | 0.8611 |
| cagr | -0.5381 |
| net_avg_win | 34.3127 |
| net_avg_loss | -56.9391 |
| avg_hold_time_bars | 6.0116 |
| exposure | 0.1404 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
