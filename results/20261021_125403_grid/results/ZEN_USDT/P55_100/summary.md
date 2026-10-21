# EMA Hourly Continuation — ZEN/USDT P55_100

**Symbol:** ZEN/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 379 |
| net_profit_factor | 0.7737 |
| net_win_rate | 0.5066 |
| gross_profit_factor | 1.0193 |
| gross_win_rate | 0.5066 |
| sharpe_ratio | -1.5234 |
| sortino_ratio | -0.4256 |
| max_drawdown | 0.3945 |
| cagr | -0.1787 |
| net_avg_win | 69.4289 |
| net_avg_loss | -92.1398 |
| avg_hold_time_bars | 8.1873 |
| exposure | 0.1410 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
