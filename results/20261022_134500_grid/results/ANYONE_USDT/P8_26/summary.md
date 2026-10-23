# EMA Hourly Continuation — ANYONE/USDT P8_26

**Symbol:** ANYONE/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1298 |
| net_profit_factor | 0.5766 |
| net_win_rate | 0.4492 |
| gross_profit_factor | 0.8883 |
| gross_win_rate | 0.4569 |
| sharpe_ratio | -7.2268 |
| sortino_ratio | -3.8598 |
| max_drawdown | 0.9862 |
| cagr | -0.8436 |
| net_avg_win | 23.0065 |
| net_avg_loss | -32.5335 |
| avg_hold_time_bars | 4.6941 |
| exposure | 0.3079 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
