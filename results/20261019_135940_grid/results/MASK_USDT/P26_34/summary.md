# EMA Hourly Continuation — MASK/USDT P26_34

**Symbol:** MASK/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1087 |
| net_profit_factor | 0.1872 |
| net_win_rate | 0.3698 |
| gross_profit_factor | 0.6299 |
| gross_win_rate | 0.4315 |
| sharpe_ratio | -13.3547 |
| sortino_ratio | -6.3950 |
| max_drawdown | 0.9998 |
| cagr | -0.9673 |
| net_avg_win | 5.7276 |
| net_avg_loss | -17.9571 |
| avg_hold_time_bars | 2.4729 |
| exposure | 0.1222 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
