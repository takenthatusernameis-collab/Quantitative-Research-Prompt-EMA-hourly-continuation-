# EMA Hourly Continuation — THETA/USDT P50_89

**Symbol:** THETA/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 676 |
| net_profit_factor | 0.4932 |
| net_win_rate | 0.4645 |
| gross_profit_factor | 0.8551 |
| gross_win_rate | 0.4704 |
| sharpe_ratio | -5.5671 |
| sortino_ratio | -2.0404 |
| max_drawdown | 0.9210 |
| cagr | -0.6312 |
| net_avg_win | 28.4665 |
| net_avg_loss | -50.0608 |
| avg_hold_time_bars | 4.3062 |
| exposure | 0.1323 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
