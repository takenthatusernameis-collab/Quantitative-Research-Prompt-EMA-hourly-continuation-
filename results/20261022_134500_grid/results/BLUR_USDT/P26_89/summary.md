# EMA Hourly Continuation — BLUR/USDT P26_89

**Symbol:** BLUR/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 676 |
| net_profit_factor | 0.6697 |
| net_win_rate | 0.4882 |
| gross_profit_factor | 1.0155 |
| gross_win_rate | 0.4970 |
| sharpe_ratio | -3.6352 |
| sortino_ratio | -1.3396 |
| max_drawdown | 0.8033 |
| cagr | -0.4675 |
| net_avg_win | 48.9137 |
| net_avg_loss | -69.6578 |
| avg_hold_time_bars | 11.2219 |
| exposure | 0.3433 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
