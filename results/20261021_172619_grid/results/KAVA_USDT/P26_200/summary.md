# EMA Hourly Continuation — KAVA/USDT P26_200

**Symbol:** KAVA/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 346 |
| net_profit_factor | 0.7189 |
| net_win_rate | 0.4855 |
| gross_profit_factor | 0.9599 |
| gross_win_rate | 0.4884 |
| sharpe_ratio | -2.0834 |
| sortino_ratio | -0.5493 |
| max_drawdown | 0.4946 |
| cagr | -0.2275 |
| net_avg_win | 72.6262 |
| net_avg_loss | -95.3446 |
| avg_hold_time_bars | 34.7457 |
| exposure | 0.5465 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
