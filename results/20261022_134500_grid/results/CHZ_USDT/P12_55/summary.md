# EMA Hourly Continuation — CHZ/USDT P12_55

**Symbol:** CHZ/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1019 |
| net_profit_factor | 0.5675 |
| net_win_rate | 0.4828 |
| gross_profit_factor | 0.9552 |
| gross_win_rate | 0.4926 |
| sharpe_ratio | -5.7483 |
| sortino_ratio | -2.5771 |
| max_drawdown | 0.9580 |
| cagr | -0.7148 |
| net_avg_win | 25.5266 |
| net_avg_loss | -41.9939 |
| avg_hold_time_bars | 8.2080 |
| exposure | 0.3802 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
