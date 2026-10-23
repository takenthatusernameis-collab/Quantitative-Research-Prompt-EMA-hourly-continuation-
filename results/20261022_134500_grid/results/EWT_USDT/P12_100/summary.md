# EMA Hourly Continuation — EWT/USDT P12_100

**Symbol:** EWT/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 743 |
| net_profit_factor | 0.4766 |
| net_win_rate | 0.4240 |
| gross_profit_factor | 0.7319 |
| gross_win_rate | 0.4347 |
| sharpe_ratio | -5.8047 |
| sortino_ratio | -2.2181 |
| max_drawdown | 0.9369 |
| cagr | -0.6564 |
| net_avg_win | 26.9299 |
| net_avg_loss | -41.5874 |
| avg_hold_time_bars | 13.1117 |
| exposure | 0.4428 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
