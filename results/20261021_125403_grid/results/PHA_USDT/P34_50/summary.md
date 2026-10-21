# EMA Hourly Continuation — PHA/USDT P34_50

**Symbol:** PHA/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 260 |
| net_profit_factor | 0.8380 |
| net_win_rate | 0.5308 |
| gross_profit_factor | 1.1215 |
| gross_win_rate | 0.5308 |
| sharpe_ratio | -0.8496 |
| sortino_ratio | -0.1980 |
| max_drawdown | 0.2308 |
| cagr | -0.0877 |
| net_avg_win | 77.1838 |
| net_avg_loss | -104.1782 |
| avg_hold_time_bars | 4.8385 |
| exposure | 0.0572 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
