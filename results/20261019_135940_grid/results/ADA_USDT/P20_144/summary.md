# EMA Hourly Continuation — ADA/USDT P20_144

**Symbol:** ADA/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 471 |
| net_profit_factor | 0.6259 |
| net_win_rate | 0.4841 |
| gross_profit_factor | 0.9697 |
| gross_win_rate | 0.4926 |
| sharpe_ratio | -3.2348 |
| sortino_ratio | -0.9840 |
| max_drawdown | 0.7055 |
| cagr | -0.3791 |
| net_avg_win | 51.2058 |
| net_avg_loss | -76.7615 |
| avg_hold_time_bars | 25.3779 |
| exposure | 0.5433 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
