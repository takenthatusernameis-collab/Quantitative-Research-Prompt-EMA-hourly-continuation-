# EMA Hourly Continuation — UMA/USDT P12_100

**Symbol:** UMA/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 682 |
| net_profit_factor | 0.6077 |
| net_win_rate | 0.4765 |
| gross_profit_factor | 0.9244 |
| gross_win_rate | 0.4868 |
| sharpe_ratio | -3.8677 |
| sortino_ratio | -1.4189 |
| max_drawdown | 0.8304 |
| cagr | -0.4933 |
| net_avg_win | 39.0276 |
| net_avg_loss | -58.4614 |
| avg_hold_time_bars | 17.3123 |
| exposure | 0.5367 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
