# EMA Hourly Continuation — EWT/USDT P100_144

**Symbol:** EWT/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 465 |
| net_profit_factor | 0.3540 |
| net_win_rate | 0.3763 |
| gross_profit_factor | 0.6276 |
| gross_win_rate | 0.3871 |
| sharpe_ratio | -6.8248 |
| sortino_ratio | -2.0826 |
| max_drawdown | 0.9322 |
| cagr | -0.6503 |
| net_avg_win | 29.0718 |
| net_avg_loss | -49.5611 |
| avg_hold_time_bars | 4.7269 |
| exposure | 0.0999 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
