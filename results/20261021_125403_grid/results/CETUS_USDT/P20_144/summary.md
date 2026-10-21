# EMA Hourly Continuation — CETUS/USDT P20_144

**Symbol:** CETUS/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 355 |
| net_profit_factor | 1.1029 |
| net_win_rate | 0.5662 |
| gross_profit_factor | 1.2855 |
| gross_win_rate | 0.5662 |
| sharpe_ratio | 0.6749 |
| sortino_ratio | 0.1855 |
| max_drawdown | 0.1496 |
| cagr | 0.0755 |
| net_avg_win | 107.4478 |
| net_avg_loss | -127.1538 |
| avg_hold_time_bars | 35.4113 |
| exposure | 0.5689 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
