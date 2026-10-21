# EMA Hourly Continuation — PHA/USDT P8_50

**Symbol:** PHA/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 706 |
| net_profit_factor | 0.8437 |
| net_win_rate | 0.5028 |
| gross_profit_factor | 1.0272 |
| gross_win_rate | 0.5028 |
| sharpe_ratio | -1.5327 |
| sortino_ratio | -0.5835 |
| max_drawdown | 0.5271 |
| cagr | -0.2378 |
| net_avg_win | 75.1760 |
| net_avg_loss | -90.1173 |
| avg_hold_time_bars | 13.1926 |
| exposure | 0.4234 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
