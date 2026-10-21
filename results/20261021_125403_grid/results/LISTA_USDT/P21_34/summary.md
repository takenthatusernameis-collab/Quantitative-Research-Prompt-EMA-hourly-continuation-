# EMA Hourly Continuation — LISTA/USDT P21_34

**Symbol:** LISTA/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 413 |
| net_profit_factor | 0.6830 |
| net_win_rate | 0.4818 |
| gross_profit_factor | 0.9558 |
| gross_win_rate | 0.4818 |
| sharpe_ratio | -2.7358 |
| sortino_ratio | -0.8230 |
| max_drawdown | 0.6100 |
| cagr | -0.3154 |
| net_avg_win | 63.5767 |
| net_avg_loss | -86.5540 |
| avg_hold_time_bars | 5.5642 |
| exposure | 0.1124 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
