# EMA Hourly Continuation — MAGIC/USDT P100_144

**Symbol:** MAGIC/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 453 |
| net_profit_factor | 0.5147 |
| net_win_rate | 0.4614 |
| gross_profit_factor | 0.9052 |
| gross_win_rate | 0.4702 |
| sharpe_ratio | -4.5406 |
| sortino_ratio | -1.3635 |
| max_drawdown | 0.8188 |
| cagr | -0.4849 |
| net_avg_win | 41.1488 |
| net_avg_loss | -68.4838 |
| avg_hold_time_bars | 4.7903 |
| exposure | 0.0986 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
