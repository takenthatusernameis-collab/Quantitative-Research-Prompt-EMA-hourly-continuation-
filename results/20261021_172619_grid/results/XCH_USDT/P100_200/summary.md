# EMA Hourly Continuation — XCH/USDT P100_200

**Symbol:** XCH/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 265 |
| net_profit_factor | 0.8198 |
| net_win_rate | 0.5057 |
| gross_profit_factor | 1.0369 |
| gross_win_rate | 0.5057 |
| sharpe_ratio | -1.0772 |
| sortino_ratio | -0.2516 |
| max_drawdown | 0.3241 |
| cagr | -0.1101 |
| net_avg_win | 86.2378 |
| net_avg_loss | -107.5999 |
| avg_hold_time_bars | 12.4264 |
| exposure | 0.1497 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
