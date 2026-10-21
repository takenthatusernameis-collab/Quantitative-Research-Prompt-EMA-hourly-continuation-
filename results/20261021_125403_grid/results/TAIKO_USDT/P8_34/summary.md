# EMA Hourly Continuation — TAIKO/USDT P8_34

**Symbol:** TAIKO/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 716 |
| net_profit_factor | 0.7613 |
| net_win_rate | 0.5070 |
| gross_profit_factor | 1.0121 |
| gross_win_rate | 0.5070 |
| sharpe_ratio | -2.4242 |
| sortino_ratio | -0.9572 |
| max_drawdown | 0.7124 |
| cagr | -0.3550 |
| net_avg_win | 56.8601 |
| net_avg_loss | -76.8072 |
| avg_hold_time_bars | 9.4818 |
| exposure | 0.3261 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
