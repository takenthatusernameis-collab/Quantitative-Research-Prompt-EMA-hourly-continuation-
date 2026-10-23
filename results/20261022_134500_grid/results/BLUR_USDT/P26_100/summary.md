# EMA Hourly Continuation — BLUR/USDT P26_100

**Symbol:** BLUR/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 619 |
| net_profit_factor | 0.6758 |
| net_win_rate | 0.4847 |
| gross_profit_factor | 1.0273 |
| gross_win_rate | 0.4976 |
| sharpe_ratio | -3.4469 |
| sortino_ratio | -1.2013 |
| max_drawdown | 0.7776 |
| cagr | -0.4404 |
| net_avg_win | 53.4193 |
| net_avg_loss | -74.3390 |
| avg_hold_time_bars | 14.2439 |
| exposure | 0.3990 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
