# EMA Hourly Continuation — CFG/USDT P55_89

**Symbol:** CFG/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 316 |
| net_profit_factor | 0.6366 |
| net_win_rate | 0.4589 |
| gross_profit_factor | 0.8253 |
| gross_win_rate | 0.4589 |
| sharpe_ratio | -2.3688 |
| sortino_ratio | -0.5982 |
| max_drawdown | 0.5104 |
| cagr | -0.2405 |
| net_avg_win | 60.2729 |
| net_avg_loss | -80.2850 |
| avg_hold_time_bars | 6.2532 |
| exposure | 0.0898 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
