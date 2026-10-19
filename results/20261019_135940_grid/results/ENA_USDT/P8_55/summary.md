# EMA Hourly Continuation — ENA/USDT P8_55

**Symbol:** ENA/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 997 |
| net_profit_factor | 0.7236 |
| net_win_rate | 0.5075 |
| gross_profit_factor | 0.9947 |
| gross_win_rate | 0.5085 |
| sharpe_ratio | -2.9292 |
| sortino_ratio | -1.3108 |
| max_drawdown | 0.8108 |
| cagr | -0.4616 |
| net_avg_win | 40.8176 |
| net_avg_loss | -58.1299 |
| avg_hold_time_bars | 10.4915 |
| exposure | 0.4755 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
