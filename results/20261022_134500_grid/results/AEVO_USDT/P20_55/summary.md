# EMA Hourly Continuation — AEVO/USDT P20_55

**Symbol:** AEVO/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 953 |
| net_profit_factor | 0.5601 |
| net_win_rate | 0.4502 |
| gross_profit_factor | 0.8892 |
| gross_win_rate | 0.4627 |
| sharpe_ratio | -6.0877 |
| sortino_ratio | -2.6469 |
| max_drawdown | 0.9617 |
| cagr | -0.7176 |
| net_avg_win | 28.4534 |
| net_avg_loss | -41.5932 |
| avg_hold_time_bars | 5.9203 |
| exposure | 0.2553 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
