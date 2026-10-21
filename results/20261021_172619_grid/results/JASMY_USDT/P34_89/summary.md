# EMA Hourly Continuation — JASMY/USDT P34_89

**Symbol:** JASMY/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 419 |
| net_profit_factor | 0.7043 |
| net_win_rate | 0.4726 |
| gross_profit_factor | 0.8853 |
| gross_win_rate | 0.4726 |
| sharpe_ratio | -2.2454 |
| sortino_ratio | -0.6550 |
| max_drawdown | 0.5414 |
| cagr | -0.2597 |
| net_avg_win | 63.7547 |
| net_avg_loss | -81.1016 |
| avg_hold_time_bars | 10.4415 |
| exposure | 0.1989 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
