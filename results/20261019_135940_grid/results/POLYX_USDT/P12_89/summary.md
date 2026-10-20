# EMA Hourly Continuation — POLYX/USDT P12_89

**Symbol:** POLYX/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 698 |
| net_profit_factor | 0.7107 |
| net_win_rate | 0.4900 |
| gross_profit_factor | 1.0255 |
| gross_win_rate | 0.5014 |
| sharpe_ratio | -3.2398 |
| sortino_ratio | -1.2076 |
| max_drawdown | 0.7799 |
| cagr | -0.4364 |
| net_avg_win | 54.8198 |
| net_avg_loss | -74.0977 |
| avg_hold_time_bars | 16.8782 |
| exposure | 0.5355 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
