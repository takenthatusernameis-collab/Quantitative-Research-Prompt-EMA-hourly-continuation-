# EMA Hourly Continuation — MOVR/USDT P50_144

**Symbol:** MOVR/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 529 |
| net_profit_factor | 0.5646 |
| net_win_rate | 0.4499 |
| gross_profit_factor | 0.8506 |
| gross_win_rate | 0.4575 |
| sharpe_ratio | -3.9004 |
| sortino_ratio | -1.2675 |
| max_drawdown | 0.7876 |
| cagr | -0.4477 |
| net_avg_win | 42.2068 |
| net_avg_loss | -61.1447 |
| avg_hold_time_bars | 11.3837 |
| exposure | 0.2737 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
