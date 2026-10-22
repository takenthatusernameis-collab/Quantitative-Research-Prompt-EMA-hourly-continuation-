# EMA Hourly Continuation — NEO/USDT P26_100

**Symbol:** NEO/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 632 |
| net_profit_factor | 0.5146 |
| net_win_rate | 0.4589 |
| gross_profit_factor | 0.8563 |
| gross_win_rate | 0.4747 |
| sharpe_ratio | -5.1086 |
| sortino_ratio | -1.8100 |
| max_drawdown | 0.8911 |
| cagr | -0.5824 |
| net_avg_win | 32.4829 |
| net_avg_loss | -53.5201 |
| avg_hold_time_bars | 13.6203 |
| exposure | 0.3913 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
