# EMA Hourly Continuation — SUPER/USDT P26_34

**Symbol:** SUPER/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 231 |
| net_profit_factor | 0.6973 |
| net_win_rate | 0.5065 |
| gross_profit_factor | 1.0499 |
| gross_win_rate | 0.5152 |
| sharpe_ratio | -1.7307 |
| sortino_ratio | -0.3771 |
| max_drawdown | 0.3823 |
| cagr | -0.1600 |
| net_avg_win | 69.8081 |
| net_avg_loss | -102.7505 |
| avg_hold_time_bars | 6.1169 |
| exposure | 0.0642 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
