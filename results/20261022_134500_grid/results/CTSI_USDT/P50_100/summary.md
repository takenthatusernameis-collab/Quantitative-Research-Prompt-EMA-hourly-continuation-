# EMA Hourly Continuation — CTSI/USDT P50_100

**Symbol:** CTSI/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 694 |
| net_profit_factor | 0.5159 |
| net_win_rate | 0.4510 |
| gross_profit_factor | 0.8573 |
| gross_win_rate | 0.4625 |
| sharpe_ratio | -5.3765 |
| sortino_ratio | -2.0106 |
| max_drawdown | 0.9098 |
| cagr | -0.6150 |
| net_avg_win | 30.9540 |
| net_avg_loss | -49.2882 |
| avg_hold_time_bars | 5.9438 |
| exposure | 0.1875 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
