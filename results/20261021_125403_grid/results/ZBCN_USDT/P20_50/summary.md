# EMA Hourly Continuation — ZBCN/USDT P20_50

**Symbol:** ZBCN/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 430 |
| net_profit_factor | 0.9131 |
| net_win_rate | 0.5279 |
| gross_profit_factor | 1.1143 |
| gross_win_rate | 0.5279 |
| sharpe_ratio | -0.5742 |
| sortino_ratio | -0.1734 |
| max_drawdown | 0.2748 |
| cagr | -0.0811 |
| net_avg_win | 87.1420 |
| net_avg_loss | -106.7235 |
| avg_hold_time_bars | 6.8791 |
| exposure | 0.1369 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
