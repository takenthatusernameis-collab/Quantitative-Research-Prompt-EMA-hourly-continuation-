# EMA Hourly Continuation — LINK/USDT P34_50

**Symbol:** LINK/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 226 |
| net_profit_factor | 0.6983 |
| net_win_rate | 0.5088 |
| gross_profit_factor | 1.0193 |
| gross_win_rate | 0.5088 |
| sharpe_ratio | -1.6126 |
| sortino_ratio | -0.3490 |
| max_drawdown | 0.3748 |
| cagr | -0.1475 |
| net_avg_win | 66.4527 |
| net_avg_loss | -98.5938 |
| avg_hold_time_bars | 5.7743 |
| exposure | 0.0593 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
