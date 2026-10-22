# EMA Hourly Continuation — XLM/USDT P21_200

**Symbol:** XLM/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 409 |
| net_profit_factor | 0.5120 |
| net_win_rate | 0.4523 |
| gross_profit_factor | 0.9205 |
| gross_win_rate | 0.4694 |
| sharpe_ratio | -4.0363 |
| sortino_ratio | -1.1408 |
| max_drawdown | 0.7644 |
| cagr | -0.4304 |
| net_avg_win | 42.9155 |
| net_avg_loss | -69.2241 |
| avg_hold_time_bars | 33.5037 |
| exposure | 0.6229 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
