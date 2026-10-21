# EMA Hourly Continuation — XPR/USDT P50_100

**Symbol:** XPR/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 245 |
| net_profit_factor | 0.5855 |
| net_win_rate | 0.4367 |
| gross_profit_factor | 0.7799 |
| gross_win_rate | 0.4367 |
| sharpe_ratio | -2.6696 |
| sortino_ratio | -0.5939 |
| max_drawdown | 0.4972 |
| cagr | -0.2395 |
| net_avg_win | 65.6384 |
| net_avg_loss | -86.9236 |
| avg_hold_time_bars | 10.6694 |
| exposure | 0.1188 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
