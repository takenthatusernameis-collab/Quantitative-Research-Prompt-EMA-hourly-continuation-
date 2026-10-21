# EMA Hourly Continuation — TWT/USDT P26_89

**Symbol:** TWT/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 521 |
| net_profit_factor | 0.7373 |
| net_win_rate | 0.5010 |
| gross_profit_factor | 1.0224 |
| gross_win_rate | 0.5010 |
| sharpe_ratio | -2.3180 |
| sortino_ratio | -0.7585 |
| max_drawdown | 0.6050 |
| cagr | -0.2942 |
| net_avg_win | 62.7250 |
| net_avg_loss | -85.3963 |
| avg_hold_time_bars | 12.2994 |
| exposure | 0.2913 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
