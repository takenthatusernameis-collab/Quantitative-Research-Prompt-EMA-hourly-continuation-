# EMA Hourly Continuation — MLK/USDT P8_34

**Symbol:** MLK/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 607 |
| net_profit_factor | 0.4597 |
| net_win_rate | 0.3871 |
| gross_profit_factor | 0.6995 |
| gross_win_rate | 0.3937 |
| sharpe_ratio | -6.1166 |
| sortino_ratio | -2.1308 |
| max_drawdown | 0.9197 |
| cagr | -0.6290 |
| net_avg_win | 33.2396 |
| net_avg_loss | -45.6761 |
| avg_hold_time_bars | 9.1301 |
| exposure | 0.2508 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
