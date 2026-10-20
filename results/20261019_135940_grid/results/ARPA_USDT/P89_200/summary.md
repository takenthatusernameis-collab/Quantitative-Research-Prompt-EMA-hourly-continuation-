# EMA Hourly Continuation — ARPA/USDT P89_200

**Symbol:** ARPA/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 448 |
| net_profit_factor | 0.5047 |
| net_win_rate | 0.4219 |
| gross_profit_factor | 0.7906 |
| gross_win_rate | 0.4330 |
| sharpe_ratio | -4.8376 |
| sortino_ratio | -1.4355 |
| max_drawdown | 0.8304 |
| cagr | -0.5017 |
| net_avg_win | 44.6073 |
| net_avg_loss | -64.4999 |
| avg_hold_time_bars | 11.1183 |
| exposure | 0.2254 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
