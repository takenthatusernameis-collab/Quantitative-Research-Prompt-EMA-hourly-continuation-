# EMA Hourly Continuation — ANYONE/USDT P12_200

**Symbol:** ANYONE/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 214 |
| net_profit_factor | 0.9885 |
| net_win_rate | 0.5280 |
| gross_profit_factor | 1.1037 |
| gross_win_rate | 0.5280 |
| sharpe_ratio | -0.0088 |
| sortino_ratio | -0.0020 |
| max_drawdown | 0.1411 |
| cagr | -0.0056 |
| net_avg_win | 95.7731 |
| net_avg_loss | -108.4027 |
| avg_hold_time_bars | 72.2383 |
| exposure | 0.7812 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
