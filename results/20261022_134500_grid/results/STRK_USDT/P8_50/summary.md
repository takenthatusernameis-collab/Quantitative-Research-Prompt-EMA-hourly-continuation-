# EMA Hourly Continuation — STRK/USDT P8_50

**Symbol:** STRK/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1103 |
| net_profit_factor | 0.6444 |
| net_win_rate | 0.4751 |
| gross_profit_factor | 0.9886 |
| gross_win_rate | 0.4814 |
| sharpe_ratio | -5.3167 |
| sortino_ratio | -2.4867 |
| max_drawdown | 0.9508 |
| cagr | -0.6953 |
| net_avg_win | 32.8363 |
| net_avg_loss | -46.1148 |
| avg_hold_time_bars | 8.9610 |
| exposure | 0.4493 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
