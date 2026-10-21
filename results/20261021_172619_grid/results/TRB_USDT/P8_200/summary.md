# EMA Hourly Continuation — TRB/USDT P8_200

**Symbol:** TRB/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 219 |
| net_profit_factor | 0.8028 |
| net_win_rate | 0.4886 |
| gross_profit_factor | 0.9348 |
| gross_win_rate | 0.4886 |
| sharpe_ratio | -0.9631 |
| sortino_ratio | -0.2024 |
| max_drawdown | 0.2581 |
| cagr | -0.0901 |
| net_avg_win | 80.6138 |
| net_avg_loss | -95.9349 |
| avg_hold_time_bars | 84.4155 |
| exposure | 0.8366 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
