# EMA Hourly Continuation — PHA/USDT P100_200

**Symbol:** PHA/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 259 |
| net_profit_factor | 0.6793 |
| net_win_rate | 0.4556 |
| gross_profit_factor | 0.8329 |
| gross_win_rate | 0.4556 |
| sharpe_ratio | -1.9198 |
| sortino_ratio | -0.4385 |
| max_drawdown | 0.4190 |
| cagr | -0.1828 |
| net_avg_win | 71.3994 |
| net_avg_loss | -87.9558 |
| avg_hold_time_bars | 11.7066 |
| exposure | 0.1378 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
