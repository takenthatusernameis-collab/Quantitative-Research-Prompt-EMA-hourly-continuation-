# EMA Hourly Continuation — SUSHI/USDT P8_21

**Symbol:** SUSHI/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1652 |
| net_profit_factor | 0.3974 |
| net_win_rate | 0.4316 |
| gross_profit_factor | 0.8903 |
| gross_win_rate | 0.4522 |
| sharpe_ratio | -11.4556 |
| sortino_ratio | -6.5567 |
| max_drawdown | 0.9997 |
| cagr | -0.9621 |
| net_avg_win | 9.2468 |
| net_avg_loss | -17.6682 |
| avg_hold_time_bars | 3.1320 |
| exposure | 0.2341 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
