# EMA Hourly Continuation — COTI/USDT P20_50

**Symbol:** COTI/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 506 |
| net_profit_factor | 0.7752 |
| net_win_rate | 0.4921 |
| gross_profit_factor | 0.9874 |
| gross_win_rate | 0.4921 |
| sharpe_ratio | -1.9776 |
| sortino_ratio | -0.6368 |
| max_drawdown | 0.5389 |
| cagr | -0.2534 |
| net_avg_win | 72.0053 |
| net_avg_loss | -89.9948 |
| avg_hold_time_bars | 7.1779 |
| exposure | 0.1651 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
