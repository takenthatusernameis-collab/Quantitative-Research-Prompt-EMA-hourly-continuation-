# EMA Hourly Continuation — ANYONE/USDT P34_200

**Symbol:** ANYONE/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 238 |
| net_profit_factor | 0.8123 |
| net_win_rate | 0.4832 |
| gross_profit_factor | 0.9155 |
| gross_win_rate | 0.4832 |
| sharpe_ratio | -1.0107 |
| sortino_ratio | -0.2336 |
| max_drawdown | 0.2874 |
| cagr | -0.1037 |
| net_avg_win | 82.4856 |
| net_avg_loss | -94.9416 |
| avg_hold_time_bars | 45.7815 |
| exposure | 0.5506 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
