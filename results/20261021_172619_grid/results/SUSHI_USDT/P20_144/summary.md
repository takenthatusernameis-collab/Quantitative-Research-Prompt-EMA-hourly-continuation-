# EMA Hourly Continuation — SUSHI/USDT P20_144

**Symbol:** SUSHI/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 398 |
| net_profit_factor | 0.8465 |
| net_win_rate | 0.5101 |
| gross_profit_factor | 1.0410 |
| gross_win_rate | 0.5101 |
| sharpe_ratio | -1.0533 |
| sortino_ratio | -0.3005 |
| max_drawdown | 0.3598 |
| cagr | -0.1316 |
| net_avg_win | 81.3655 |
| net_avg_loss | -100.0591 |
| avg_hold_time_bars | 28.9422 |
| exposure | 0.5212 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
