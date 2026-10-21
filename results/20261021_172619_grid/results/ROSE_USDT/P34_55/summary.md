# EMA Hourly Continuation — ROSE/USDT P34_55

**Symbol:** ROSE/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 315 |
| net_profit_factor | 0.8087 |
| net_win_rate | 0.5206 |
| gross_profit_factor | 1.0855 |
| gross_win_rate | 0.5206 |
| sharpe_ratio | -1.2007 |
| sortino_ratio | -0.3072 |
| max_drawdown | 0.3755 |
| cagr | -0.1320 |
| net_avg_win | 77.1164 |
| net_avg_loss | -103.5700 |
| avg_hold_time_bars | 5.8159 |
| exposure | 0.0833 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
