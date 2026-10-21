# EMA Hourly Continuation — ALGO/USDT P89_100

**Symbol:** ALGO/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 87 |
| net_profit_factor | 0.7053 |
| net_win_rate | 0.5057 |
| gross_profit_factor | 1.0070 |
| gross_win_rate | 0.5057 |
| sharpe_ratio | -0.9587 |
| sortino_ratio | -0.1287 |
| max_drawdown | 0.1543 |
| cagr | -0.0568 |
| net_avg_win | 74.2300 |
| net_avg_loss | -107.6934 |
| avg_hold_time_bars | 4.7586 |
| exposure | 0.0188 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
