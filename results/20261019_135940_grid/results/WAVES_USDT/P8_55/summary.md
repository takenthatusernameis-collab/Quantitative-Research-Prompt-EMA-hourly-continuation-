# EMA Hourly Continuation — WAVES/USDT P8_55

**Symbol:** WAVES/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1257 |
| net_profit_factor | 0.5078 |
| net_win_rate | 0.4320 |
| gross_profit_factor | 0.9351 |
| gross_win_rate | 0.4614 |
| sharpe_ratio | -8.8172 |
| sortino_ratio | -4.3848 |
| max_drawdown | 0.9959 |
| cagr | -0.8860 |
| net_avg_win | 18.9223 |
| net_avg_loss | -28.3361 |
| avg_hold_time_bars | 8.2267 |
| exposure | 0.4700 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
