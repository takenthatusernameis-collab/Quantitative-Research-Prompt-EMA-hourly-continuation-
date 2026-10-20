# EMA Hourly Continuation — UQC/USDT P20_100

**Symbol:** UQC/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 305 |
| net_profit_factor | 0.2823 |
| net_win_rate | 0.3016 |
| gross_profit_factor | 0.4941 |
| gross_win_rate | 0.3246 |
| sharpe_ratio | -6.7916 |
| sortino_ratio | -1.6539 |
| max_drawdown | 0.8958 |
| cagr | -0.5920 |
| net_avg_win | 38.2912 |
| net_avg_loss | -58.5941 |
| avg_hold_time_bars | 43.3344 |
| exposure | 0.5982 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
