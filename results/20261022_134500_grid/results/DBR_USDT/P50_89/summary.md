# EMA Hourly Continuation — DBR/USDT P50_89

**Symbol:** DBR/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 435 |
| net_profit_factor | 0.4657 |
| net_win_rate | 0.4322 |
| gross_profit_factor | 0.9061 |
| gross_win_rate | 0.4598 |
| sharpe_ratio | -6.0190 |
| sortino_ratio | -1.9742 |
| max_drawdown | 0.8689 |
| cagr | -0.6256 |
| net_avg_win | 39.9120 |
| net_avg_loss | -65.2292 |
| avg_hold_time_bars | 6.6414 |
| exposure | 0.1643 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
