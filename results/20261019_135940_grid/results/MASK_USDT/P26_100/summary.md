# EMA Hourly Continuation — MASK/USDT P26_100

**Symbol:** MASK/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 702 |
| net_profit_factor | 0.4673 |
| net_win_rate | 0.4573 |
| gross_profit_factor | 0.8072 |
| gross_win_rate | 0.4772 |
| sharpe_ratio | -5.5405 |
| sortino_ratio | -2.0691 |
| max_drawdown | 0.9245 |
| cagr | -0.6327 |
| net_avg_win | 25.1170 |
| net_avg_loss | -45.2866 |
| avg_hold_time_bars | 10.4473 |
| exposure | 0.3334 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
