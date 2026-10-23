# EMA Hourly Continuation — CELO/USDT P20_50

**Symbol:** CELO/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 948 |
| net_profit_factor | 0.4649 |
| net_win_rate | 0.4409 |
| gross_profit_factor | 0.7977 |
| gross_win_rate | 0.4557 |
| sharpe_ratio | -6.9178 |
| sortino_ratio | -3.0104 |
| max_drawdown | 0.9738 |
| cagr | -0.7630 |
| net_avg_win | 20.2325 |
| net_avg_loss | -34.3256 |
| avg_hold_time_bars | 5.6466 |
| exposure | 0.2422 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
