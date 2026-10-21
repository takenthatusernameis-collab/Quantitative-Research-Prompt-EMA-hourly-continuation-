# EMA Hourly Continuation — SAND/USDT P50_200

**Symbol:** SAND/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 287 |
| net_profit_factor | 0.8145 |
| net_win_rate | 0.5052 |
| gross_profit_factor | 1.0162 |
| gross_win_rate | 0.5052 |
| sharpe_ratio | -1.0780 |
| sortino_ratio | -0.2617 |
| max_drawdown | 0.2805 |
| cagr | -0.1145 |
| net_avg_win | 79.6968 |
| net_avg_loss | -99.9100 |
| avg_hold_time_bars | 31.0523 |
| exposure | 0.4051 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
