# EMA Hourly Continuation — CWEB/USDT P12_26

**Symbol:** CWEB/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1267 |
| net_profit_factor | 0.2509 |
| net_win_rate | 0.2691 |
| gross_profit_factor | 0.6511 |
| gross_win_rate | 0.2991 |
| sharpe_ratio | -18.0351 |
| sortino_ratio | -9.5322 |
| max_drawdown | 1.0000 |
| cagr | -0.9946 |
| net_avg_win | 9.8237 |
| net_avg_loss | -14.4167 |
| avg_hold_time_bars | 4.8745 |
| exposure | 0.2807 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
