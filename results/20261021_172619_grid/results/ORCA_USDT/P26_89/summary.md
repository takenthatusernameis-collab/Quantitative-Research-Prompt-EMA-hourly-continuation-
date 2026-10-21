# EMA Hourly Continuation — ORCA/USDT P26_89

**Symbol:** ORCA/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 502 |
| net_profit_factor | 0.8306 |
| net_win_rate | 0.5219 |
| gross_profit_factor | 1.0744 |
| gross_win_rate | 0.5219 |
| sharpe_ratio | -1.2955 |
| sortino_ratio | -0.4163 |
| max_drawdown | 0.4517 |
| cagr | -0.1773 |
| net_avg_win | 72.5409 |
| net_avg_loss | -95.3377 |
| avg_hold_time_bars | 13.4622 |
| exposure | 0.3072 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
