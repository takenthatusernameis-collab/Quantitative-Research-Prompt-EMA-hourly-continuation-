# EMA Hourly Continuation — BLUR/USDT P26_200

**Symbol:** BLUR/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 282 |
| net_profit_factor | 1.0105 |
| net_win_rate | 0.5496 |
| gross_profit_factor | 1.2016 |
| gross_win_rate | 0.5496 |
| sharpe_ratio | 0.1076 |
| sortino_ratio | 0.0261 |
| max_drawdown | 0.1373 |
| cagr | 0.0058 |
| net_avg_win | 91.4722 |
| net_avg_loss | -110.4807 |
| avg_hold_time_bars | 49.8652 |
| exposure | 0.6363 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
