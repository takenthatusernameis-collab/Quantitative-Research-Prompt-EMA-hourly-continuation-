# EMA Hourly Continuation — STRAX/USDT P21_200

**Symbol:** STRAX/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 568 |
| net_profit_factor | 0.5346 |
| net_win_rate | 0.4102 |
| gross_profit_factor | 0.7455 |
| gross_win_rate | 0.4137 |
| sharpe_ratio | -5.2502 |
| sortino_ratio | -1.7672 |
| max_drawdown | 0.8765 |
| cagr | -0.5674 |
| net_avg_win | 43.2147 |
| net_avg_loss | -56.2222 |
| avg_hold_time_bars | 21.1444 |
| exposure | 0.5491 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
