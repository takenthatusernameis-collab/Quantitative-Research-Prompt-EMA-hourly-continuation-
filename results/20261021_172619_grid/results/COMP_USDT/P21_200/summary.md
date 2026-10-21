# EMA Hourly Continuation — COMP/USDT P21_200

**Symbol:** COMP/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 314 |
| net_profit_factor | 0.7594 |
| net_win_rate | 0.4904 |
| gross_profit_factor | 0.9454 |
| gross_win_rate | 0.4904 |
| sharpe_ratio | -1.4101 |
| sortino_ratio | -0.3569 |
| max_drawdown | 0.3722 |
| cagr | -0.1519 |
| net_avg_win | 69.4377 |
| net_avg_loss | -88.0054 |
| avg_hold_time_bars | 44.2420 |
| exposure | 0.6315 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
