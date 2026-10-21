# EMA Hourly Continuation — KMNO/USDT P55_200

**Symbol:** KMNO/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 287 |
| net_profit_factor | 0.7734 |
| net_win_rate | 0.4843 |
| gross_profit_factor | 0.9491 |
| gross_win_rate | 0.4843 |
| sharpe_ratio | -1.4348 |
| sortino_ratio | -0.3489 |
| max_drawdown | 0.3392 |
| cagr | -0.1497 |
| net_avg_win | 81.0890 |
| net_avg_loss | -98.4768 |
| avg_hold_time_bars | 25.3484 |
| exposure | 0.3359 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
