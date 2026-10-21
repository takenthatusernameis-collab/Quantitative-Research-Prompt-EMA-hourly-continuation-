# EMA Hourly Continuation — PROM/USDT P26_200

**Symbol:** PROM/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 352 |
| net_profit_factor | 0.5183 |
| net_win_rate | 0.4062 |
| gross_profit_factor | 0.6786 |
| gross_win_rate | 0.4091 |
| sharpe_ratio | -3.7619 |
| sortino_ratio | -0.9937 |
| max_drawdown | 0.7062 |
| cagr | -0.3705 |
| net_avg_win | 51.7238 |
| net_avg_loss | -68.2747 |
| avg_hold_time_bars | 32.4460 |
| exposure | 0.5191 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
