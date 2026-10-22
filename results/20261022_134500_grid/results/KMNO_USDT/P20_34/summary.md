# EMA Hourly Continuation — KMNO/USDT P20_34

**Symbol:** KMNO/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 934 |
| net_profit_factor | 0.4219 |
| net_win_rate | 0.4272 |
| gross_profit_factor | 0.8291 |
| gross_win_rate | 0.4475 |
| sharpe_ratio | -8.7306 |
| sortino_ratio | -3.8074 |
| max_drawdown | 0.9909 |
| cagr | -0.8507 |
| net_avg_win | 18.1270 |
| net_avg_loss | -32.0409 |
| avg_hold_time_bars | 3.2238 |
| exposure | 0.1390 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
