# EMA Hourly Continuation — TAIKO/USDT P26_55

**Symbol:** TAIKO/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 426 |
| net_profit_factor | 0.6771 |
| net_win_rate | 0.4836 |
| gross_profit_factor | 0.9452 |
| gross_win_rate | 0.4836 |
| sharpe_ratio | -2.7850 |
| sortino_ratio | -0.8456 |
| max_drawdown | 0.6423 |
| cagr | -0.3216 |
| net_avg_win | 61.3129 |
| net_avg_loss | -84.7898 |
| avg_hold_time_bars | 7.5329 |
| exposure | 0.1541 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
