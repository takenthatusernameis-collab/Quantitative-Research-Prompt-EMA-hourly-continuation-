# EMA Hourly Continuation — EGLD/USDT P26_100

**Symbol:** EGLD/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 470 |
| net_profit_factor | 0.7834 |
| net_win_rate | 0.5043 |
| gross_profit_factor | 1.0076 |
| gross_win_rate | 0.5043 |
| sharpe_ratio | -1.6024 |
| sortino_ratio | -0.4983 |
| max_drawdown | 0.4945 |
| cagr | -0.2054 |
| net_avg_win | 66.9376 |
| net_avg_loss | -86.9117 |
| avg_hold_time_bars | 16.3149 |
| exposure | 0.3485 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
