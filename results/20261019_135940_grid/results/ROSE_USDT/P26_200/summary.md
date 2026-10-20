# EMA Hourly Continuation — ROSE/USDT P26_200

**Symbol:** ROSE/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 375 |
| net_profit_factor | 0.8704 |
| net_win_rate | 0.5333 |
| gross_profit_factor | 1.1316 |
| gross_win_rate | 0.5333 |
| sharpe_ratio | -0.8365 |
| sortino_ratio | -0.2323 |
| max_drawdown | 0.3215 |
| cagr | -0.1047 |
| net_avg_win | 81.4032 |
| net_avg_loss | -106.8872 |
| avg_hold_time_bars | 34.7760 |
| exposure | 0.5928 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
