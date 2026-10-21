# EMA Hourly Continuation — CVX/USDT P34_100

**Symbol:** CVX/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 450 |
| net_profit_factor | 0.7662 |
| net_win_rate | 0.4911 |
| gross_profit_factor | 0.9646 |
| gross_win_rate | 0.4911 |
| sharpe_ratio | -1.7913 |
| sortino_ratio | -0.5432 |
| max_drawdown | 0.4747 |
| cagr | -0.2213 |
| net_avg_win | 69.1451 |
| net_avg_loss | -87.0955 |
| avg_hold_time_bars | 12.5400 |
| exposure | 0.2565 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
