# EMA Hourly Continuation — CTSI/USDT P21_89

**Symbol:** CTSI/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 776 |
| net_profit_factor | 0.5995 |
| net_win_rate | 0.4369 |
| gross_profit_factor | 0.9319 |
| gross_win_rate | 0.4485 |
| sharpe_ratio | -5.7048 |
| sortino_ratio | -2.2397 |
| max_drawdown | 0.9338 |
| cagr | -0.6563 |
| net_avg_win | 41.1403 |
| net_avg_loss | -53.2319 |
| avg_hold_time_bars | 10.6482 |
| exposure | 0.3756 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
