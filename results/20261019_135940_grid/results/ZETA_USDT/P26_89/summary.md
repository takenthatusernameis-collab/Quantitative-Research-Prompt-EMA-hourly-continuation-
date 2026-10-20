# EMA Hourly Continuation — ZETA/USDT P26_89

**Symbol:** ZETA/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 668 |
| net_profit_factor | 0.6933 |
| net_win_rate | 0.4910 |
| gross_profit_factor | 1.0457 |
| gross_win_rate | 0.4970 |
| sharpe_ratio | -3.6174 |
| sortino_ratio | -1.3082 |
| max_drawdown | 0.8068 |
| cagr | -0.4692 |
| net_avg_win | 54.9663 |
| net_avg_loss | -76.4868 |
| avg_hold_time_bars | 11.3129 |
| exposure | 0.3420 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
