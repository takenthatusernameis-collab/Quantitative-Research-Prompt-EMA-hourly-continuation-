# EMA Hourly Continuation — TFUEL/USDT P8_100

**Symbol:** TFUEL/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 675 |
| net_profit_factor | 0.7026 |
| net_win_rate | 0.4563 |
| gross_profit_factor | 0.8852 |
| gross_win_rate | 0.4563 |
| sharpe_ratio | -3.3827 |
| sortino_ratio | -1.2452 |
| max_drawdown | 0.7705 |
| cagr | -0.4355 |
| net_avg_win | 58.5796 |
| net_avg_loss | -69.9706 |
| avg_hold_time_bars | 18.8074 |
| exposure | 0.5745 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
