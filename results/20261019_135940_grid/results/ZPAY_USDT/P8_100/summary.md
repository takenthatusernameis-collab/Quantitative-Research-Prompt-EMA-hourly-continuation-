# EMA Hourly Continuation — ZPAY/USDT P8_100

**Symbol:** ZPAY/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 481 |
| net_profit_factor | 0.4943 |
| net_win_rate | 0.3514 |
| gross_profit_factor | 0.6151 |
| gross_win_rate | 0.3514 |
| sharpe_ratio | -5.3694 |
| sortino_ratio | -1.6364 |
| max_drawdown | 0.8615 |
| cagr | -0.5353 |
| net_avg_win | 49.4760 |
| net_avg_loss | -54.2135 |
| avg_hold_time_bars | 29.3306 |
| exposure | 0.6384 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
