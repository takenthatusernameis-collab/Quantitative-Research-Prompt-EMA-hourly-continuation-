# EMA Hourly Continuation — ZBCN/USDT P20_100

**Symbol:** ZBCN/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 824 |
| net_profit_factor | 0.6996 |
| net_win_rate | 0.5012 |
| gross_profit_factor | 1.0133 |
| gross_win_rate | 0.5012 |
| sharpe_ratio | -3.2529 |
| sortino_ratio | -1.3228 |
| max_drawdown | 0.8100 |
| cagr | -0.4724 |
| net_avg_win | 44.7542 |
| net_avg_loss | -64.2784 |
| avg_hold_time_bars | 9.7937 |
| exposure | 0.3734 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
