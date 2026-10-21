# EMA Hourly Continuation — EGLD/USDT P12_34

**Symbol:** EGLD/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 623 |
| net_profit_factor | 0.7089 |
| net_win_rate | 0.4896 |
| gross_profit_factor | 0.9851 |
| gross_win_rate | 0.4896 |
| sharpe_ratio | -2.9217 |
| sortino_ratio | -1.0452 |
| max_drawdown | 0.7175 |
| cagr | -0.3805 |
| net_avg_win | 55.8544 |
| net_avg_loss | -75.5706 |
| avg_hold_time_bars | 6.6051 |
| exposure | 0.1870 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
