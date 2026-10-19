# EMA Hourly Continuation — DCR/USDT P55_89

**Symbol:** DCR/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 696 |
| net_profit_factor | 0.3946 |
| net_win_rate | 0.4282 |
| gross_profit_factor | 0.7643 |
| gross_win_rate | 0.4454 |
| sharpe_ratio | -7.1528 |
| sortino_ratio | -2.6710 |
| max_drawdown | 0.9630 |
| cagr | -0.7291 |
| net_avg_win | 21.0606 |
| net_avg_loss | -39.9630 |
| avg_hold_time_bars | 4.7601 |
| exposure | 0.1499 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
