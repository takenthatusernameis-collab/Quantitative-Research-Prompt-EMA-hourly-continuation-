# EMA Hourly Continuation — LSK/USDT P12_50

**Symbol:** LSK/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 899 |
| net_profit_factor | 0.5878 |
| net_win_rate | 0.4772 |
| gross_profit_factor | 1.0148 |
| gross_win_rate | 0.4828 |
| sharpe_ratio | -5.3416 |
| sortino_ratio | -2.2573 |
| max_drawdown | 0.9349 |
| cagr | -0.6606 |
| net_avg_win | 31.0379 |
| net_avg_loss | -48.1964 |
| avg_hold_time_bars | 8.3293 |
| exposure | 0.3404 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
