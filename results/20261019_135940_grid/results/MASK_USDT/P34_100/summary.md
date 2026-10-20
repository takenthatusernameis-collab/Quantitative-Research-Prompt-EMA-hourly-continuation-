# EMA Hourly Continuation — MASK/USDT P34_100

**Symbol:** MASK/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 697 |
| net_profit_factor | 0.4438 |
| net_win_rate | 0.4548 |
| gross_profit_factor | 0.8169 |
| gross_win_rate | 0.4821 |
| sharpe_ratio | -5.7081 |
| sortino_ratio | -2.1309 |
| max_drawdown | 0.9289 |
| cagr | -0.6427 |
| net_avg_win | 23.2701 |
| net_avg_loss | -43.7428 |
| avg_hold_time_bars | 8.5308 |
| exposure | 0.2703 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
