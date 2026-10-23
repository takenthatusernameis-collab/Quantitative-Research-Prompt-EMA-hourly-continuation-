# EMA Hourly Continuation — AEVO/USDT P8_50

**Symbol:** AEVO/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1027 |
| net_profit_factor | 0.6038 |
| net_win_rate | 0.4654 |
| gross_profit_factor | 0.8970 |
| gross_win_rate | 0.4732 |
| sharpe_ratio | -5.3805 |
| sortino_ratio | -2.4123 |
| max_drawdown | 0.9491 |
| cagr | -0.6881 |
| net_avg_win | 30.1913 |
| net_avg_loss | -43.5377 |
| avg_hold_time_bars | 10.9260 |
| exposure | 0.5078 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
