# EMA Hourly Continuation — AAVE/USDT P21_50

**Symbol:** AAVE/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 442 |
| net_profit_factor | 0.6649 |
| net_win_rate | 0.4683 |
| gross_profit_factor | 0.8824 |
| gross_win_rate | 0.4683 |
| sharpe_ratio | -2.7028 |
| sortino_ratio | -0.8108 |
| max_drawdown | 0.6108 |
| cagr | -0.3102 |
| net_avg_win | 58.1243 |
| net_avg_loss | -77.0054 |
| avg_hold_time_bars | 7.8597 |
| exposure | 0.1579 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
