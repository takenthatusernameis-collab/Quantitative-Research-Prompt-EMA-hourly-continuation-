# EMA Hourly Continuation — CHZ/USDT P12_50

**Symbol:** CHZ/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1093 |
| net_profit_factor | 0.5141 |
| net_win_rate | 0.4639 |
| gross_profit_factor | 0.9038 |
| gross_win_rate | 0.4767 |
| sharpe_ratio | -6.9209 |
| sortino_ratio | -3.2073 |
| max_drawdown | 0.9811 |
| cagr | -0.7936 |
| net_avg_win | 20.4692 |
| net_avg_loss | -34.4503 |
| avg_hold_time_bars | 7.0814 |
| exposure | 0.3518 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
