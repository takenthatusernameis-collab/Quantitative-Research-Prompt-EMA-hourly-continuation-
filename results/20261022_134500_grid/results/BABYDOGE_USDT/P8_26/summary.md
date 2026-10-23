# EMA Hourly Continuation — BABYDOGE/USDT P8_26

**Symbol:** BABYDOGE/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 45 |
| net_profit_factor | 1.0298 |
| net_win_rate | 0.5333 |
| gross_profit_factor | 1.1316 |
| gross_win_rate | 0.5333 |
| sharpe_ratio | 0.0830 |
| sortino_ratio | 0.0080 |
| max_drawdown | 0.0338 |
| cagr | 0.0026 |
| net_avg_win | 94.8566 |
| net_avg_loss | -105.2660 |
| avg_hold_time_bars | 9.4000 |
| exposure | 0.0191 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
