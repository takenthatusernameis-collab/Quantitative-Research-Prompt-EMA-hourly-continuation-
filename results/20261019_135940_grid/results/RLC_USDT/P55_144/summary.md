# EMA Hourly Continuation — RLC/USDT P55_144

**Symbol:** RLC/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 518 |
| net_profit_factor | 0.5594 |
| net_win_rate | 0.4653 |
| gross_profit_factor | 0.8699 |
| gross_win_rate | 0.4749 |
| sharpe_ratio | -3.8552 |
| sortino_ratio | -1.2408 |
| max_drawdown | 0.7846 |
| cagr | -0.4454 |
| net_avg_win | 40.7012 |
| net_avg_loss | -63.2989 |
| avg_hold_time_bars | 10.2432 |
| exposure | 0.2412 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
