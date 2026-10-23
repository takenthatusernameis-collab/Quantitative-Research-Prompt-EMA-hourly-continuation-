# EMA Hourly Continuation — DODO/USDT P12_21

**Symbol:** DODO/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1525 |
| net_profit_factor | 0.3380 |
| net_win_rate | 0.4079 |
| gross_profit_factor | 0.8069 |
| gross_win_rate | 0.4354 |
| sharpe_ratio | -12.4758 |
| sortino_ratio | -6.9014 |
| max_drawdown | 0.9998 |
| cagr | -0.9688 |
| net_avg_win | 8.2066 |
| net_avg_loss | -16.7253 |
| avg_hold_time_bars | 2.5692 |
| exposure | 0.1773 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
