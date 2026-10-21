# EMA Hourly Continuation — VET/USDT P12_100

**Symbol:** VET/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 502 |
| net_profit_factor | 0.8513 |
| net_win_rate | 0.5219 |
| gross_profit_factor | 1.0789 |
| gross_win_rate | 0.5219 |
| sharpe_ratio | -1.1028 |
| sortino_ratio | -0.3552 |
| max_drawdown | 0.4103 |
| cagr | -0.1536 |
| net_avg_win | 74.8052 |
| net_avg_loss | -95.9215 |
| avg_hold_time_bars | 24.0876 |
| exposure | 0.5496 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
