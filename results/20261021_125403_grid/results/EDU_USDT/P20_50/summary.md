# EMA Hourly Continuation — EDU/USDT P20_50

**Symbol:** EDU/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 612 |
| net_profit_factor | 0.6230 |
| net_win_rate | 0.4624 |
| gross_profit_factor | 0.8270 |
| gross_win_rate | 0.4641 |
| sharpe_ratio | -3.3409 |
| sortino_ratio | -1.1753 |
| max_drawdown | 0.7529 |
| cagr | -0.4170 |
| net_avg_win | 43.4160 |
| net_avg_loss | -59.9474 |
| avg_hold_time_bars | 7.1748 |
| exposure | 0.1987 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
