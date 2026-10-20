# EMA Hourly Continuation — ATH/USDT P100_200

**Symbol:** ATH/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 389 |
| net_profit_factor | 0.5301 |
| net_win_rate | 0.4499 |
| gross_profit_factor | 0.8157 |
| gross_win_rate | 0.4524 |
| sharpe_ratio | -4.0298 |
| sortino_ratio | -1.1512 |
| max_drawdown | 0.7401 |
| cagr | -0.4301 |
| net_avg_win | 47.3146 |
| net_avg_loss | -72.9928 |
| avg_hold_time_bars | 9.6941 |
| exposure | 0.1828 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
