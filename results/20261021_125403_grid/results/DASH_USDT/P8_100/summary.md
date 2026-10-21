# EMA Hourly Continuation — DASH/USDT P8_100

**Symbol:** DASH/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 478 |
| net_profit_factor | 0.7682 |
| net_win_rate | 0.4895 |
| gross_profit_factor | 0.9634 |
| gross_win_rate | 0.4895 |
| sharpe_ratio | -1.7859 |
| sortino_ratio | -0.5575 |
| max_drawdown | 0.5077 |
| cagr | -0.2273 |
| net_avg_win | 67.5208 |
| net_avg_loss | -84.2915 |
| avg_hold_time_bars | 30.1485 |
| exposure | 0.6550 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
