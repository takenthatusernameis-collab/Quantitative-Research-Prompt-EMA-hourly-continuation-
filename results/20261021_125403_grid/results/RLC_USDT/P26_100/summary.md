# EMA Hourly Continuation — RLC/USDT P26_100

**Symbol:** RLC/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 508 |
| net_profit_factor | 0.7925 |
| net_win_rate | 0.5118 |
| gross_profit_factor | 1.0380 |
| gross_win_rate | 0.5118 |
| sharpe_ratio | -1.6634 |
| sortino_ratio | -0.5376 |
| max_drawdown | 0.5069 |
| cagr | -0.2198 |
| net_avg_win | 68.1168 |
| net_avg_loss | -90.1151 |
| avg_hold_time_bars | 13.8720 |
| exposure | 0.3203 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
