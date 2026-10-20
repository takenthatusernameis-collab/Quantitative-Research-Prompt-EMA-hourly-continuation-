# EMA Hourly Continuation — MERL/USDT P34_89

**Symbol:** MERL/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 655 |
| net_profit_factor | 0.6834 |
| net_win_rate | 0.4870 |
| gross_profit_factor | 0.9497 |
| gross_win_rate | 0.4916 |
| sharpe_ratio | -3.0211 |
| sortino_ratio | -1.1013 |
| max_drawdown | 0.7409 |
| cagr | -0.3998 |
| net_avg_win | 48.8205 |
| net_avg_loss | -67.8256 |
| avg_hold_time_bars | 8.1908 |
| exposure | 0.2445 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
