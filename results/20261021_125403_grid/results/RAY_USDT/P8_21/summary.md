# EMA Hourly Continuation — RAY/USDT P8_21

**Symbol:** RAY/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 587 |
| net_profit_factor | 0.8742 |
| net_win_rate | 0.5434 |
| gross_profit_factor | 1.1771 |
| gross_win_rate | 0.5434 |
| sharpe_ratio | -0.9572 |
| sortino_ratio | -0.3353 |
| max_drawdown | 0.4044 |
| cagr | -0.1471 |
| net_avg_win | 71.7636 |
| net_avg_loss | -97.7141 |
| avg_hold_time_bars | 6.0392 |
| exposure | 0.1611 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
