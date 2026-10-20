# EMA Hourly Continuation — POPCAT/USDT P20_200

**Symbol:** POPCAT/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 341 |
| net_profit_factor | 0.7779 |
| net_win_rate | 0.4956 |
| gross_profit_factor | 1.0104 |
| gross_win_rate | 0.5015 |
| sharpe_ratio | -1.6780 |
| sortino_ratio | -0.4696 |
| max_drawdown | 0.4340 |
| cagr | -0.2013 |
| net_avg_win | 79.7581 |
| net_avg_loss | -100.7395 |
| avg_hold_time_bars | 35.8651 |
| exposure | 0.6461 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
