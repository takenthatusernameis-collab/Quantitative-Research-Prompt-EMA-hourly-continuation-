# EMA Hourly Continuation — SWFTC/USDT P50_100

**Symbol:** SWFTC/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 642 |
| net_profit_factor | 0.4823 |
| net_win_rate | 0.4221 |
| gross_profit_factor | 0.8878 |
| gross_win_rate | 0.4424 |
| sharpe_ratio | -6.7550 |
| sortino_ratio | -2.4061 |
| max_drawdown | 0.9532 |
| cagr | -0.7036 |
| net_avg_win | 32.7582 |
| net_avg_loss | -49.6114 |
| avg_hold_time_bars | 5.2617 |
| exposure | 0.1535 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
