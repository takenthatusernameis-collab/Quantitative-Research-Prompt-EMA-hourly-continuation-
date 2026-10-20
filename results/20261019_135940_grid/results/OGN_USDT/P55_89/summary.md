# EMA Hourly Continuation — OGN/USDT P55_89

**Symbol:** OGN/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 689 |
| net_profit_factor | 0.3890 |
| net_win_rate | 0.4194 |
| gross_profit_factor | 0.7571 |
| gross_win_rate | 0.4398 |
| sharpe_ratio | -7.3923 |
| sortino_ratio | -2.7349 |
| max_drawdown | 0.9684 |
| cagr | -0.7447 |
| net_avg_win | 21.3221 |
| net_avg_loss | -39.6070 |
| avg_hold_time_bars | 4.9260 |
| exposure | 0.1536 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
