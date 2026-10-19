# EMA Hourly Continuation — EIGEN/USDT P50_89

**Symbol:** EIGEN/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 584 |
| net_profit_factor | 0.5637 |
| net_win_rate | 0.4709 |
| gross_profit_factor | 0.8810 |
| gross_win_rate | 0.4777 |
| sharpe_ratio | -4.7333 |
| sortino_ratio | -1.7815 |
| max_drawdown | 0.8317 |
| cagr | -0.5787 |
| net_avg_win | 39.0000 |
| net_avg_loss | -61.5759 |
| avg_hold_time_bars | 4.4983 |
| exposure | 0.1462 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
