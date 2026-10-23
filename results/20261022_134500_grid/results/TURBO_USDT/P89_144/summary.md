# EMA Hourly Continuation — TURBO/USDT P89_144

**Symbol:** TURBO/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 443 |
| net_profit_factor | 0.5770 |
| net_win_rate | 0.4605 |
| gross_profit_factor | 0.8685 |
| gross_win_rate | 0.4718 |
| sharpe_ratio | -4.0784 |
| sortino_ratio | -1.3337 |
| max_drawdown | 0.7513 |
| cagr | -0.4695 |
| net_avg_win | 49.1125 |
| net_avg_loss | -72.6558 |
| avg_hold_time_bars | 4.7223 |
| exposure | 0.1141 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
