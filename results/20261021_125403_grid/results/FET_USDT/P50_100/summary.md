# EMA Hourly Continuation — FET/USDT P50_100

**Symbol:** FET/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 304 |
| net_profit_factor | 0.7811 |
| net_win_rate | 0.4967 |
| gross_profit_factor | 0.9680 |
| gross_win_rate | 0.4967 |
| sharpe_ratio | -1.2825 |
| sortino_ratio | -0.3197 |
| max_drawdown | 0.3399 |
| cagr | -0.1371 |
| net_avg_win | 73.1556 |
| net_avg_loss | -92.4312 |
| avg_hold_time_bars | 10.5428 |
| exposure | 0.1457 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
