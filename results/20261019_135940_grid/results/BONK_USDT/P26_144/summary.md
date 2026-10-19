# EMA Hourly Continuation — BONK/USDT P26_144

**Symbol:** BONK/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 461 |
| net_profit_factor | 0.6459 |
| net_win_rate | 0.4707 |
| gross_profit_factor | 0.8781 |
| gross_win_rate | 0.4751 |
| sharpe_ratio | -2.9163 |
| sortino_ratio | -0.8726 |
| max_drawdown | 0.7178 |
| cagr | -0.3468 |
| net_avg_win | 55.2162 |
| net_avg_loss | -76.0245 |
| avg_hold_time_bars | 23.9826 |
| exposure | 0.5025 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
