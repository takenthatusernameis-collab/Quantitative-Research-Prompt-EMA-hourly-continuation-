# EMA Hourly Continuation — ELON/USDT P21_50

**Symbol:** ELON/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 951 |
| net_profit_factor | 0.3832 |
| net_win_rate | 0.4111 |
| gross_profit_factor | 0.7172 |
| gross_win_rate | 0.4185 |
| sharpe_ratio | -8.9327 |
| sortino_ratio | -3.9306 |
| max_drawdown | 0.9917 |
| cagr | -0.8511 |
| net_avg_win | 15.7539 |
| net_avg_loss | -28.7073 |
| avg_hold_time_bars | 4.4606 |
| exposure | 0.1928 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
