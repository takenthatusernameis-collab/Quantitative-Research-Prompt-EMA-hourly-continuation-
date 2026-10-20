# EMA Hourly Continuation — BABYDOGE/USDT P21_89

**Symbol:** BABYDOGE/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 53 |
| net_profit_factor | 1.0380 |
| net_win_rate | 0.5283 |
| gross_profit_factor | 1.1095 |
| gross_win_rate | 0.5283 |
| sharpe_ratio | 0.1073 |
| sortino_ratio | 0.0112 |
| max_drawdown | 0.0523 |
| cagr | 0.0039 |
| net_avg_win | 95.5455 |
| net_avg_loss | -103.0944 |
| avg_hold_time_bars | 58.1132 |
| exposure | 0.1394 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
