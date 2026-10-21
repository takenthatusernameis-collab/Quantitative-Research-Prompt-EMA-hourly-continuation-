# EMA Hourly Continuation — MASK/USDT P26_89

**Symbol:** MASK/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 511 |
| net_profit_factor | 0.5873 |
| net_win_rate | 0.4658 |
| gross_profit_factor | 0.8328 |
| gross_win_rate | 0.4697 |
| sharpe_ratio | -3.3910 |
| sortino_ratio | -1.0900 |
| max_drawdown | 0.7330 |
| cagr | -0.3974 |
| net_avg_win | 43.0427 |
| net_avg_loss | -63.8898 |
| avg_hold_time_bars | 12.4892 |
| exposure | 0.2901 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
