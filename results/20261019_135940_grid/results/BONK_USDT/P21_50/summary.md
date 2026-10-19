# EMA Hourly Continuation — BONK/USDT P21_50

**Symbol:** BONK/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 971 |
| net_profit_factor | 0.4896 |
| net_win_rate | 0.4583 |
| gross_profit_factor | 0.8272 |
| gross_win_rate | 0.4727 |
| sharpe_ratio | -6.5549 |
| sortino_ratio | -2.8492 |
| max_drawdown | 0.9735 |
| cagr | -0.7598 |
| net_avg_win | 20.9553 |
| net_avg_loss | -36.2109 |
| avg_hold_time_bars | 4.6643 |
| exposure | 0.2059 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
