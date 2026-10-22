# EMA Hourly Continuation — XCH/USDT P8_200

**Symbol:** XCH/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 367 |
| net_profit_factor | 0.8557 |
| net_win_rate | 0.5068 |
| gross_profit_factor | 1.0194 |
| gross_win_rate | 0.5068 |
| sharpe_ratio | -0.8932 |
| sortino_ratio | -0.2452 |
| max_drawdown | 0.2732 |
| cagr | -0.1096 |
| net_avg_win | 80.5879 |
| net_avg_loss | -96.7807 |
| avg_hold_time_bars | 45.6213 |
| exposure | 0.7610 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
