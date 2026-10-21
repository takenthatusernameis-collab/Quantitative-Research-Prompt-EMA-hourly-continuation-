# EMA Hourly Continuation — IOST/USDT P26_200

**Symbol:** IOST/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 309 |
| net_profit_factor | 0.9836 |
| net_win_rate | 0.5566 |
| gross_profit_factor | 1.2397 |
| gross_win_rate | 0.5566 |
| sharpe_ratio | -0.0354 |
| sortino_ratio | -0.0090 |
| max_drawdown | 0.1987 |
| cagr | -0.0100 |
| net_avg_win | 87.2393 |
| net_avg_loss | -111.3497 |
| avg_hold_time_bars | 40.9968 |
| exposure | 0.5758 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
