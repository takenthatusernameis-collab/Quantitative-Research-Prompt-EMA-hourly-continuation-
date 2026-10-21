# EMA Hourly Continuation — TAIKO/USDT P12_21

**Symbol:** TAIKO/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 343 |
| net_profit_factor | 0.8122 |
| net_win_rate | 0.5481 |
| gross_profit_factor | 1.2192 |
| gross_win_rate | 0.5481 |
| sharpe_ratio | -1.3162 |
| sortino_ratio | -0.3625 |
| max_drawdown | 0.4091 |
| cagr | -0.1541 |
| net_avg_win | 75.4794 |
| net_avg_loss | -112.7149 |
| avg_hold_time_bars | 5.7784 |
| exposure | 0.0952 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
