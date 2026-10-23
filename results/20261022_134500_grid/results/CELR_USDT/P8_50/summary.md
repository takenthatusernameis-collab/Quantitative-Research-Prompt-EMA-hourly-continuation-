# EMA Hourly Continuation — CELR/USDT P8_50

**Symbol:** CELR/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1030 |
| net_profit_factor | 0.5795 |
| net_win_rate | 0.4563 |
| gross_profit_factor | 0.9129 |
| gross_win_rate | 0.4680 |
| sharpe_ratio | -5.7775 |
| sortino_ratio | -2.6060 |
| max_drawdown | 0.9569 |
| cagr | -0.7104 |
| net_avg_win | 28.0316 |
| net_avg_loss | -40.6003 |
| avg_hold_time_bars | 10.4670 |
| exposure | 0.4879 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
