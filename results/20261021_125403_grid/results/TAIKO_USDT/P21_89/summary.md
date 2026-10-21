# EMA Hourly Continuation — TAIKO/USDT P21_89

**Symbol:** TAIKO/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 447 |
| net_profit_factor | 0.8679 |
| net_win_rate | 0.5324 |
| gross_profit_factor | 1.1217 |
| gross_win_rate | 0.5324 |
| sharpe_ratio | -0.9064 |
| sortino_ratio | -0.2842 |
| max_drawdown | 0.3555 |
| cagr | -0.1256 |
| net_avg_win | 75.3969 |
| net_avg_loss | -98.9265 |
| avg_hold_time_bars | 17.5839 |
| exposure | 0.3776 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
