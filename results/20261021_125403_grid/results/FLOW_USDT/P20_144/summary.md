# EMA Hourly Continuation — FLOW/USDT P20_144

**Symbol:** FLOW/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 343 |
| net_profit_factor | 0.8135 |
| net_win_rate | 0.4985 |
| gross_profit_factor | 0.9935 |
| gross_win_rate | 0.4985 |
| sharpe_ratio | -1.2290 |
| sortino_ratio | -0.3252 |
| max_drawdown | 0.3540 |
| cagr | -0.1404 |
| net_avg_win | 80.6311 |
| net_avg_loss | -98.5361 |
| avg_hold_time_bars | 36.3703 |
| exposure | 0.5670 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
