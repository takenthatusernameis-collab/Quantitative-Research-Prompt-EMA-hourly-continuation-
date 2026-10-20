# EMA Hourly Continuation — NYM/USDT P50_100

**Symbol:** NYM/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 534 |
| net_profit_factor | 0.2162 |
| net_win_rate | 0.3258 |
| gross_profit_factor | 0.5541 |
| gross_win_rate | 0.3614 |
| sharpe_ratio | -9.5273 |
| sortino_ratio | -3.1868 |
| max_drawdown | 0.9854 |
| cagr | -0.8121 |
| net_avg_win | 15.6109 |
| net_avg_loss | -34.9059 |
| avg_hold_time_bars | 7.1648 |
| exposure | 0.1739 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
