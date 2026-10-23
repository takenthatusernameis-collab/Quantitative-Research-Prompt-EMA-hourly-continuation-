# EMA Hourly Continuation — BIGTIME/USDT P50_55

**Symbol:** BIGTIME/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 778 |
| net_profit_factor | 0.2751 |
| net_win_rate | 0.3946 |
| gross_profit_factor | 0.7163 |
| gross_win_rate | 0.4499 |
| sharpe_ratio | -10.3293 |
| sortino_ratio | -4.1590 |
| max_drawdown | 0.9960 |
| cagr | -0.8879 |
| net_avg_win | 12.3133 |
| net_avg_loss | -29.1723 |
| avg_hold_time_bars | 2.4961 |
| exposure | 0.0879 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
