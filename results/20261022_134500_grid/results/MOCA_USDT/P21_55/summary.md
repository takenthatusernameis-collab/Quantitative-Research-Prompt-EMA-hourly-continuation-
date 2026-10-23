# EMA Hourly Continuation — MOCA/USDT P21_55

**Symbol:** MOCA/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 833 |
| net_profit_factor | 0.5335 |
| net_win_rate | 0.4490 |
| gross_profit_factor | 0.8952 |
| gross_win_rate | 0.4658 |
| sharpe_ratio | -6.6588 |
| sortino_ratio | -2.8205 |
| max_drawdown | 0.9610 |
| cagr | -0.7520 |
| net_avg_win | 29.3020 |
| net_avg_loss | -44.7513 |
| avg_hold_time_bars | 5.1321 |
| exposure | 0.2143 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
