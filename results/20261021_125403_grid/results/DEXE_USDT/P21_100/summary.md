# EMA Hourly Continuation — DEXE/USDT P21_100

**Symbol:** DEXE/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 403 |
| net_profit_factor | 0.7681 |
| net_win_rate | 0.4938 |
| gross_profit_factor | 0.9416 |
| gross_win_rate | 0.4938 |
| sharpe_ratio | -1.4523 |
| sortino_ratio | -0.4162 |
| max_drawdown | 0.4523 |
| cagr | -0.1755 |
| net_avg_win | 63.9279 |
| net_avg_loss | -81.1883 |
| avg_hold_time_bars | 29.3127 |
| exposure | 0.5370 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
