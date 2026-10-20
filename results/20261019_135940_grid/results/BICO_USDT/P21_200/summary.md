# EMA Hourly Continuation — BICO/USDT P21_200

**Symbol:** BICO/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 337 |
| net_profit_factor | 0.6714 |
| net_win_rate | 0.4599 |
| gross_profit_factor | 0.8686 |
| gross_win_rate | 0.4659 |
| sharpe_ratio | -2.3288 |
| sortino_ratio | -0.6030 |
| max_drawdown | 0.5408 |
| cagr | -0.2465 |
| net_avg_win | 67.0653 |
| net_avg_loss | -85.0707 |
| avg_hold_time_bars | 41.6736 |
| exposure | 0.6384 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
