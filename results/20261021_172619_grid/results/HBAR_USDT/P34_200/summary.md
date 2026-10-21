# EMA Hourly Continuation — HBAR/USDT P34_200

**Symbol:** HBAR/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 284 |
| net_profit_factor | 0.8766 |
| net_win_rate | 0.5211 |
| gross_profit_factor | 1.0774 |
| gross_win_rate | 0.5211 |
| sharpe_ratio | -0.6935 |
| sortino_ratio | -0.1679 |
| max_drawdown | 0.2845 |
| cagr | -0.0765 |
| net_avg_win | 86.8904 |
| net_avg_loss | -107.8712 |
| avg_hold_time_bars | 38.7113 |
| exposure | 0.4997 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
