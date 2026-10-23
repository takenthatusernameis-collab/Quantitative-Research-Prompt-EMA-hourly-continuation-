# EMA Hourly Continuation — OGN/USDT P34_55

**Symbol:** OGN/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 898 |
| net_profit_factor | 0.4161 |
| net_win_rate | 0.4165 |
| gross_profit_factor | 0.8923 |
| gross_win_rate | 0.4488 |
| sharpe_ratio | -9.1513 |
| sortino_ratio | -3.9004 |
| max_drawdown | 0.9928 |
| cagr | -0.8568 |
| net_avg_win | 18.9093 |
| net_avg_loss | -32.4386 |
| avg_hold_time_bars | 3.7361 |
| exposure | 0.1518 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
