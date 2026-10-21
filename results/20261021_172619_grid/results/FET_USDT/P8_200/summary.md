# EMA Hourly Continuation — FET/USDT P8_200

**Symbol:** FET/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 253 |
| net_profit_factor | 1.0215 |
| net_win_rate | 0.5375 |
| gross_profit_factor | 1.1426 |
| gross_win_rate | 0.5375 |
| sharpe_ratio | 0.1565 |
| sortino_ratio | 0.0359 |
| max_drawdown | 0.1392 |
| cagr | 0.0107 |
| net_avg_win | 94.8570 |
| net_avg_loss | -107.9413 |
| avg_hold_time_bars | 71.1265 |
| exposure | 0.8180 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
