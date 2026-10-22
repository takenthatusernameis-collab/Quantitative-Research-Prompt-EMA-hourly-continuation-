# EMA Hourly Continuation — EWT/USDT P21_144

**Symbol:** EWT/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 432 |
| net_profit_factor | 0.6957 |
| net_win_rate | 0.4606 |
| gross_profit_factor | 0.8357 |
| gross_win_rate | 0.4606 |
| sharpe_ratio | -2.2604 |
| sortino_ratio | -0.6659 |
| max_drawdown | 0.5984 |
| cagr | -0.2645 |
| net_avg_win | 61.7646 |
| net_avg_loss | -75.8270 |
| avg_hold_time_bars | 20.9144 |
| exposure | 0.4107 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
