# EMA Hourly Continuation — POLYX/USDT P34_89

**Symbol:** POLYX/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 672 |
| net_profit_factor | 0.6315 |
| net_win_rate | 0.4747 |
| gross_profit_factor | 1.0081 |
| gross_win_rate | 0.4940 |
| sharpe_ratio | -4.2317 |
| sortino_ratio | -1.5464 |
| max_drawdown | 0.8566 |
| cagr | -0.5205 |
| net_avg_win | 45.2411 |
| net_avg_loss | -64.7395 |
| avg_hold_time_bars | 8.3988 |
| exposure | 0.2565 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
