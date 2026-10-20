# EMA Hourly Continuation — ARPA/USDT P21_26

**Symbol:** ARPA/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1249 |
| net_profit_factor | 0.2204 |
| net_win_rate | 0.3507 |
| gross_profit_factor | 0.7426 |
| gross_win_rate | 0.4131 |
| sharpe_ratio | -14.7410 |
| sortino_ratio | -7.5818 |
| max_drawdown | 1.0000 |
| cagr | -0.9807 |
| net_avg_win | 6.4553 |
| net_avg_loss | -15.8162 |
| avg_hold_time_bars | 2.4051 |
| exposure | 0.1359 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
