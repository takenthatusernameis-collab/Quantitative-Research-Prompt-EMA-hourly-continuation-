# EMA Hourly Continuation — AAVE/USDT P21_200

**Symbol:** AAVE/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 381 |
| net_profit_factor | 0.8137 |
| net_win_rate | 0.5302 |
| gross_profit_factor | 1.1234 |
| gross_win_rate | 0.5354 |
| sharpe_ratio | -1.1072 |
| sortino_ratio | -0.3082 |
| max_drawdown | 0.4284 |
| cagr | -0.1358 |
| net_avg_win | 66.3651 |
| net_avg_loss | -92.0392 |
| avg_hold_time_bars | 36.1129 |
| exposure | 0.6254 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
