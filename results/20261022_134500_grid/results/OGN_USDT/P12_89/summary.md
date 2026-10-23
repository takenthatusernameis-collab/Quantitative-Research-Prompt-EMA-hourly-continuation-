# EMA Hourly Continuation — OGN/USDT P12_89

**Symbol:** OGN/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 708 |
| net_profit_factor | 0.5762 |
| net_win_rate | 0.4492 |
| gross_profit_factor | 0.9070 |
| gross_win_rate | 0.4619 |
| sharpe_ratio | -5.2489 |
| sortino_ratio | -1.9475 |
| max_drawdown | 0.9105 |
| cagr | -0.6132 |
| net_avg_win | 38.8564 |
| net_avg_loss | -54.9894 |
| avg_hold_time_bars | 17.1342 |
| exposure | 0.5489 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
