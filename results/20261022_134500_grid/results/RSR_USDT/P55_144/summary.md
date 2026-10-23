# EMA Hourly Continuation — RSR/USDT P55_144

**Symbol:** RSR/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 469 |
| net_profit_factor | 0.7265 |
| net_win_rate | 0.5096 |
| gross_profit_factor | 1.0561 |
| gross_win_rate | 0.5160 |
| sharpe_ratio | -2.0724 |
| sortino_ratio | -0.6360 |
| max_drawdown | 0.5348 |
| cagr | -0.2599 |
| net_avg_win | 58.9453 |
| net_avg_loss | -84.3126 |
| avg_hold_time_bars | 11.8273 |
| exposure | 0.2521 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
