# EMA Hourly Continuation — DOGS/USDT P34_55

**Symbol:** DOGS/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 801 |
| net_profit_factor | 0.4453 |
| net_win_rate | 0.4195 |
| gross_profit_factor | 0.7490 |
| gross_win_rate | 0.4332 |
| sharpe_ratio | -8.4747 |
| sortino_ratio | -3.6445 |
| max_drawdown | 0.9806 |
| cagr | -0.8382 |
| net_avg_win | 23.4162 |
| net_avg_loss | -37.9985 |
| avg_hold_time_bars | 3.0250 |
| exposure | 0.1285 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
