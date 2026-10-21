# EMA Hourly Continuation — GLM/USDT P26_100

**Symbol:** GLM/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 520 |
| net_profit_factor | 0.6770 |
| net_win_rate | 0.4827 |
| gross_profit_factor | 0.9114 |
| gross_win_rate | 0.4827 |
| sharpe_ratio | -2.6995 |
| sortino_ratio | -0.8766 |
| max_drawdown | 0.6500 |
| cagr | -0.3327 |
| net_avg_win | 53.2610 |
| net_avg_loss | -73.4126 |
| avg_hold_time_bars | 14.4538 |
| exposure | 0.3416 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
