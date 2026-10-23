# EMA Hourly Continuation — REQ/USDT P26_55

**Symbol:** REQ/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1047 |
| net_profit_factor | 0.3644 |
| net_win_rate | 0.3859 |
| gross_profit_factor | 0.8098 |
| gross_win_rate | 0.4231 |
| sharpe_ratio | -11.3224 |
| sortino_ratio | -5.2413 |
| max_drawdown | 0.9988 |
| cagr | -0.9298 |
| net_avg_win | 14.1746 |
| net_avg_loss | -24.4384 |
| avg_hold_time_bars | 4.8214 |
| exposure | 0.2295 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
