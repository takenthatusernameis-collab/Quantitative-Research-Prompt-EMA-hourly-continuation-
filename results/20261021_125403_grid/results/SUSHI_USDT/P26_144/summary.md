# EMA Hourly Continuation — SUSHI/USDT P26_144

**Symbol:** SUSHI/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 382 |
| net_profit_factor | 0.8098 |
| net_win_rate | 0.4974 |
| gross_profit_factor | 0.9893 |
| gross_win_rate | 0.4974 |
| sharpe_ratio | -1.3010 |
| sortino_ratio | -0.3627 |
| max_drawdown | 0.3765 |
| cagr | -0.1554 |
| net_avg_win | 77.7319 |
| net_avg_loss | -94.9906 |
| avg_hold_time_bars | 27.2304 |
| exposure | 0.4707 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
