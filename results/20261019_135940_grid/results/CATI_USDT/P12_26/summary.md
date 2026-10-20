# EMA Hourly Continuation — CATI/USDT P12_26

**Symbol:** CATI/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1238 |
| net_profit_factor | 0.3662 |
| net_win_rate | 0.3724 |
| gross_profit_factor | 0.6491 |
| gross_win_rate | 0.3966 |
| sharpe_ratio | -13.7811 |
| sortino_ratio | -7.5580 |
| max_drawdown | 0.9997 |
| cagr | -0.9796 |
| net_avg_win | 12.5279 |
| net_avg_loss | -20.2991 |
| avg_hold_time_bars | 3.1987 |
| exposure | 0.2171 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
