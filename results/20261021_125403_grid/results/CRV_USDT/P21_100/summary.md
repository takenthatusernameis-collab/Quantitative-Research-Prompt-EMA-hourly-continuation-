# EMA Hourly Continuation — CRV/USDT P21_100

**Symbol:** CRV/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 458 |
| net_profit_factor | 0.8828 |
| net_win_rate | 0.5197 |
| gross_profit_factor | 1.0812 |
| gross_win_rate | 0.5197 |
| sharpe_ratio | -0.8467 |
| sortino_ratio | -0.2608 |
| max_drawdown | 0.3243 |
| cagr | -0.1163 |
| net_avg_win | 84.4858 |
| net_avg_loss | -103.5320 |
| avg_hold_time_bars | 16.5218 |
| exposure | 0.3440 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
