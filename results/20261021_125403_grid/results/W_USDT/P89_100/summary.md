# EMA Hourly Continuation — W/USDT P89_100

**Symbol:** W/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 120 |
| net_profit_factor | 0.7556 |
| net_win_rate | 0.5083 |
| gross_profit_factor | 1.0118 |
| gross_win_rate | 0.5083 |
| sharpe_ratio | -0.8867 |
| sortino_ratio | -0.1397 |
| max_drawdown | 0.1744 |
| cagr | -0.0621 |
| net_avg_win | 75.4330 |
| net_avg_loss | -103.2113 |
| avg_hold_time_bars | 4.3583 |
| exposure | 0.0238 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
