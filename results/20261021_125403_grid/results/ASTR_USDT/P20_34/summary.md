# EMA Hourly Continuation — ASTR/USDT P20_34

**Symbol:** ASTR/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 452 |
| net_profit_factor | 0.6991 |
| net_win_rate | 0.5177 |
| gross_profit_factor | 1.1199 |
| gross_win_rate | 0.5243 |
| sharpe_ratio | -2.5953 |
| sortino_ratio | -0.7912 |
| max_drawdown | 0.6391 |
| cagr | -0.3051 |
| net_avg_win | 59.6542 |
| net_avg_loss | -91.5900 |
| avg_hold_time_bars | 5.5929 |
| exposure | 0.1144 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
