# EMA Hourly Continuation — IOTA/USDT P26_89

**Symbol:** IOTA/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 727 |
| net_profit_factor | 0.5409 |
| net_win_rate | 0.4443 |
| gross_profit_factor | 0.8781 |
| gross_win_rate | 0.4525 |
| sharpe_ratio | -5.5261 |
| sortino_ratio | -2.0948 |
| max_drawdown | 0.9266 |
| cagr | -0.6357 |
| net_avg_win | 33.5923 |
| net_avg_loss | -49.6494 |
| avg_hold_time_bars | 9.1541 |
| exposure | 0.3025 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
