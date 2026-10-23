# EMA Hourly Continuation — PIXEL/USDT P8_12

**Symbol:** PIXEL/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1810 |
| net_profit_factor | 0.2427 |
| net_win_rate | 0.3823 |
| gross_profit_factor | 0.6973 |
| gross_win_rate | 0.4254 |
| sharpe_ratio | -15.6186 |
| sortino_ratio | -9.4452 |
| max_drawdown | 1.0000 |
| cagr | -0.9925 |
| net_avg_win | 4.6313 |
| net_avg_loss | -11.8111 |
| avg_hold_time_bars | 2.1343 |
| exposure | 0.1748 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
