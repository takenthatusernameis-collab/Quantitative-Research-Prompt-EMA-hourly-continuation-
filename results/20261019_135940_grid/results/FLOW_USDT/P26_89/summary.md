# EMA Hourly Continuation — FLOW/USDT P26_89

**Symbol:** FLOW/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 728 |
| net_profit_factor | 0.5026 |
| net_win_rate | 0.4451 |
| gross_profit_factor | 0.8398 |
| gross_win_rate | 0.4533 |
| sharpe_ratio | -5.8586 |
| sortino_ratio | -2.2197 |
| max_drawdown | 0.9373 |
| cagr | -0.6626 |
| net_avg_win | 29.1529 |
| net_avg_loss | -46.5157 |
| avg_hold_time_bars | 9.2706 |
| exposure | 0.3068 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
