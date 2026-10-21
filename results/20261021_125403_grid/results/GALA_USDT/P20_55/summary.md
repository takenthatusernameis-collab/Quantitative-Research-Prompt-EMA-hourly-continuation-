# EMA Hourly Continuation — GALA/USDT P20_55

**Symbol:** GALA/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 537 |
| net_profit_factor | 0.7040 |
| net_win_rate | 0.4749 |
| gross_profit_factor | 0.9100 |
| gross_win_rate | 0.4749 |
| sharpe_ratio | -2.6371 |
| sortino_ratio | -0.8724 |
| max_drawdown | 0.6567 |
| cagr | -0.3294 |
| net_avg_win | 59.0956 |
| net_avg_loss | -75.9007 |
| avg_hold_time_bars | 7.5568 |
| exposure | 0.1845 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
