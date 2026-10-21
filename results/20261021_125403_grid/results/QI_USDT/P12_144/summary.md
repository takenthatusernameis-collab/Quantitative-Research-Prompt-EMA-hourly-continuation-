# EMA Hourly Continuation — QI/USDT P12_144

**Symbol:** QI/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 388 |
| net_profit_factor | 0.7371 |
| net_win_rate | 0.4794 |
| gross_profit_factor | 0.9170 |
| gross_win_rate | 0.4794 |
| sharpe_ratio | -1.8713 |
| sortino_ratio | -0.5240 |
| max_drawdown | 0.4793 |
| cagr | -0.2143 |
| net_avg_win | 68.7002 |
| net_avg_loss | -85.8219 |
| avg_hold_time_bars | 36.8196 |
| exposure | 0.6465 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
