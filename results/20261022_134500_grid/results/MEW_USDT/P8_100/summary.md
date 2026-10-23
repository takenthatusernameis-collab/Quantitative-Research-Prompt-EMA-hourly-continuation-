# EMA Hourly Continuation — MEW/USDT P8_100

**Symbol:** MEW/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 648 |
| net_profit_factor | 0.6262 |
| net_win_rate | 0.4660 |
| gross_profit_factor | 0.8561 |
| gross_win_rate | 0.4691 |
| sharpe_ratio | -3.8947 |
| sortino_ratio | -1.3840 |
| max_drawdown | 0.8340 |
| cagr | -0.4898 |
| net_avg_win | 45.2377 |
| net_avg_loss | -63.0525 |
| avg_hold_time_bars | 22.1250 |
| exposure | 0.6517 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
