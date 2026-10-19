# EMA Hourly Continuation — SHIB/USDT P50_100

**Symbol:** SHIB/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 635 |
| net_profit_factor | 0.4744 |
| net_win_rate | 0.4472 |
| gross_profit_factor | 0.9282 |
| gross_win_rate | 0.4630 |
| sharpe_ratio | -6.2787 |
| sortino_ratio | -2.2340 |
| max_drawdown | 0.9394 |
| cagr | -0.6662 |
| net_avg_win | 29.7632 |
| net_avg_loss | -50.7604 |
| avg_hold_time_bars | 5.7039 |
| exposure | 0.1646 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
