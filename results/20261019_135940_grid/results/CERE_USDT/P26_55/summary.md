# EMA Hourly Continuation — CERE/USDT P26_55

**Symbol:** CERE/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 958 |
| net_profit_factor | 0.3838 |
| net_win_rate | 0.3267 |
| gross_profit_factor | 0.7556 |
| gross_win_rate | 0.3685 |
| sharpe_ratio | -12.7959 |
| sortino_ratio | -5.6902 |
| max_drawdown | 0.9995 |
| cagr | -0.9512 |
| net_avg_win | 19.8851 |
| net_avg_loss | -25.1456 |
| avg_hold_time_bars | 5.9718 |
| exposure | 0.2600 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
