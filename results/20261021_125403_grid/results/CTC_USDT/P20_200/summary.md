# EMA Hourly Continuation — CTC/USDT P20_200

**Symbol:** CTC/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 374 |
| net_profit_factor | 0.8047 |
| net_win_rate | 0.5080 |
| gross_profit_factor | 1.0161 |
| gross_win_rate | 0.5080 |
| sharpe_ratio | -1.2687 |
| sortino_ratio | -0.3509 |
| max_drawdown | 0.4519 |
| cagr | -0.1509 |
| net_avg_win | 73.0724 |
| net_avg_loss | -93.7687 |
| avg_hold_time_bars | 33.9652 |
| exposure | 0.5774 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
