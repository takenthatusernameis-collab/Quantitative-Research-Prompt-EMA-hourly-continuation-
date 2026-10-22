# EMA Hourly Continuation — PEOPLE/USDT P21_200

**Symbol:** PEOPLE/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 301 |
| net_profit_factor | 1.0130 |
| net_win_rate | 0.5449 |
| gross_profit_factor | 1.1896 |
| gross_win_rate | 0.5449 |
| sharpe_ratio | 0.1248 |
| sortino_ratio | 0.0313 |
| max_drawdown | 0.1502 |
| cagr | 0.0077 |
| net_avg_win | 92.7245 |
| net_avg_loss | -109.5751 |
| avg_hold_time_bars | 45.5914 |
| exposure | 0.6210 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
