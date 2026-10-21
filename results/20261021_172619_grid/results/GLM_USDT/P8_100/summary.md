# EMA Hourly Continuation — GLM/USDT P8_100

**Symbol:** GLM/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 571 |
| net_profit_factor | 0.7780 |
| net_win_rate | 0.5044 |
| gross_profit_factor | 1.0114 |
| gross_win_rate | 0.5044 |
| sharpe_ratio | -1.8645 |
| sortino_ratio | -0.6376 |
| max_drawdown | 0.5506 |
| cagr | -0.2548 |
| net_avg_win | 63.5482 |
| net_avg_loss | -83.1219 |
| avg_hold_time_bars | 24.5044 |
| exposure | 0.6360 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
