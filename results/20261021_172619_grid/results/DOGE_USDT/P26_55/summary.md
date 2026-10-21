# EMA Hourly Continuation — DOGE/USDT P26_55

**Symbol:** DOGE/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 388 |
| net_profit_factor | 0.6315 |
| net_win_rate | 0.4691 |
| gross_profit_factor | 0.8738 |
| gross_win_rate | 0.4691 |
| sharpe_ratio | -2.7944 |
| sortino_ratio | -0.7868 |
| max_drawdown | 0.5964 |
| cagr | -0.3025 |
| net_avg_win | 56.0592 |
| net_avg_loss | -78.4260 |
| avg_hold_time_bars | 7.7912 |
| exposure | 0.1374 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
