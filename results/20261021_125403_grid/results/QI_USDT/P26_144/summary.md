# EMA Hourly Continuation — QI/USDT P26_144

**Symbol:** QI/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 385 |
| net_profit_factor | 0.7426 |
| net_win_rate | 0.4831 |
| gross_profit_factor | 0.9458 |
| gross_win_rate | 0.4857 |
| sharpe_ratio | -1.8437 |
| sortino_ratio | -0.5152 |
| max_drawdown | 0.4859 |
| cagr | -0.2114 |
| net_avg_win | 69.9187 |
| net_avg_loss | -88.0014 |
| avg_hold_time_bars | 24.3558 |
| exposure | 0.4243 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
