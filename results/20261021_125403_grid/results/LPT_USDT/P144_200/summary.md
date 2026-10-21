# EMA Hourly Continuation — LPT/USDT P144_200

**Symbol:** LPT/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 217 |
| net_profit_factor | 0.6878 |
| net_win_rate | 0.4747 |
| gross_profit_factor | 0.9065 |
| gross_win_rate | 0.4747 |
| sharpe_ratio | -1.7527 |
| sortino_ratio | -0.3689 |
| max_drawdown | 0.3724 |
| cagr | -0.1556 |
| net_avg_win | 73.9965 |
| net_avg_loss | -97.2103 |
| avg_hold_time_bars | 8.0230 |
| exposure | 0.0791 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
