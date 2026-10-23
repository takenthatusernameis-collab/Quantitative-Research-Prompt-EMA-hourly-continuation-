# EMA Hourly Continuation — ANYONE/USDT P89_100

**Symbol:** ANYONE/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 502 |
| net_profit_factor | 0.3661 |
| net_win_rate | 0.3944 |
| gross_profit_factor | 0.7176 |
| gross_win_rate | 0.4124 |
| sharpe_ratio | -7.4231 |
| sortino_ratio | -2.5031 |
| max_drawdown | 0.9399 |
| cagr | -0.7109 |
| net_avg_win | 27.4004 |
| net_avg_loss | -48.7468 |
| avg_hold_time_bars | 2.6295 |
| exposure | 0.0667 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
