# EMA Hourly Continuation — BNB/USDT P100_200

**Symbol:** BNB/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 263 |
| net_profit_factor | 0.6337 |
| net_win_rate | 0.5247 |
| gross_profit_factor | 1.0821 |
| gross_win_rate | 0.5247 |
| sharpe_ratio | -2.1396 |
| sortino_ratio | -0.5020 |
| max_drawdown | 0.4396 |
| cagr | -0.2032 |
| net_avg_win | 54.4884 |
| net_avg_loss | -94.9293 |
| avg_hold_time_bars | 12.1293 |
| exposure | 0.1450 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
