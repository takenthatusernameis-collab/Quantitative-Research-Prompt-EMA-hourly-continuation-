# EMA Hourly Continuation — IOTX/USDT P26_100

**Symbol:** IOTX/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 450 |
| net_profit_factor | 0.7579 |
| net_win_rate | 0.4956 |
| gross_profit_factor | 0.9620 |
| gross_win_rate | 0.4956 |
| sharpe_ratio | -1.7672 |
| sortino_ratio | -0.5365 |
| max_drawdown | 0.4916 |
| cagr | -0.2185 |
| net_avg_win | 64.7992 |
| net_avg_loss | -83.9899 |
| avg_hold_time_bars | 16.3911 |
| exposure | 0.3353 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
