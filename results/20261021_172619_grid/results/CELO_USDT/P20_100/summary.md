# EMA Hourly Continuation — CELO/USDT P20_100

**Symbol:** CELO/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 458 |
| net_profit_factor | 0.8466 |
| net_win_rate | 0.5066 |
| gross_profit_factor | 1.0441 |
| gross_win_rate | 0.5066 |
| sharpe_ratio | -1.2310 |
| sortino_ratio | -0.3770 |
| max_drawdown | 0.4594 |
| cagr | -0.1611 |
| net_avg_win | 85.1503 |
| net_avg_loss | -103.2544 |
| avg_hold_time_bars | 21.9323 |
| exposure | 0.4545 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
