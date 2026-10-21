# EMA Hourly Continuation — POLYX/USDT P26_55

**Symbol:** POLYX/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 532 |
| net_profit_factor | 0.7222 |
| net_win_rate | 0.4981 |
| gross_profit_factor | 1.0183 |
| gross_win_rate | 0.4981 |
| sharpe_ratio | -2.6729 |
| sortino_ratio | -0.8838 |
| max_drawdown | 0.6717 |
| cagr | -0.3335 |
| net_avg_win | 62.6722 |
| net_avg_loss | -86.1337 |
| avg_hold_time_bars | 6.6259 |
| exposure | 0.1602 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
