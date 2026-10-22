# EMA Hourly Continuation — COMP/USDT P21_100

**Symbol:** COMP/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 665 |
| net_profit_factor | 0.5261 |
| net_win_rate | 0.4752 |
| gross_profit_factor | 0.8461 |
| gross_win_rate | 0.4827 |
| sharpe_ratio | -4.3609 |
| sortino_ratio | -1.5684 |
| max_drawdown | 0.8648 |
| cagr | -0.5366 |
| net_avg_win | 30.0340 |
| net_avg_loss | -51.6944 |
| avg_hold_time_bars | 14.8842 |
| exposure | 0.4499 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
