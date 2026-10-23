# EMA Hourly Continuation — POLYX/USDT P12_200

**Symbol:** POLYX/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 367 |
| net_profit_factor | 0.7256 |
| net_win_rate | 0.5041 |
| gross_profit_factor | 1.0095 |
| gross_win_rate | 0.5068 |
| sharpe_ratio | -1.8189 |
| sortino_ratio | -0.4904 |
| max_drawdown | 0.4765 |
| cagr | -0.2091 |
| net_avg_win | 63.6399 |
| net_avg_loss | -89.1539 |
| avg_hold_time_bars | 44.2125 |
| exposure | 0.7375 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
