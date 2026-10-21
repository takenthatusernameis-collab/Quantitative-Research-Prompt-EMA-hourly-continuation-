# EMA Hourly Continuation — SUPER/USDT P144_200

**Symbol:** SUPER/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 198 |
| net_profit_factor | 0.5701 |
| net_win_rate | 0.4343 |
| gross_profit_factor | 0.7578 |
| gross_win_rate | 0.4343 |
| sharpe_ratio | -2.4444 |
| sortino_ratio | -0.4875 |
| max_drawdown | 0.4385 |
| cagr | -0.2024 |
| net_avg_win | 66.8229 |
| net_avg_loss | -90.0025 |
| avg_hold_time_bars | 7.0152 |
| exposure | 0.0631 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
