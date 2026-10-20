# EMA Hourly Continuation — STRAX/USDT P26_89

**Symbol:** STRAX/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 779 |
| net_profit_factor | 0.5308 |
| net_win_rate | 0.4172 |
| gross_profit_factor | 0.8410 |
| gross_win_rate | 0.4300 |
| sharpe_ratio | -6.9554 |
| sortino_ratio | -2.7315 |
| max_drawdown | 0.9648 |
| cagr | -0.7376 |
| net_avg_win | 33.5749 |
| net_avg_loss | -45.2813 |
| avg_hold_time_bars | 9.2811 |
| exposure | 0.3306 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
