# EMA Hourly Continuation — XCH/USDT P8_100

**Symbol:** XCH/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 553 |
| net_profit_factor | 0.8323 |
| net_win_rate | 0.5063 |
| gross_profit_factor | 1.0152 |
| gross_win_rate | 0.5063 |
| sharpe_ratio | -1.2617 |
| sortino_ratio | -0.4254 |
| max_drawdown | 0.4093 |
| cagr | -0.1804 |
| net_avg_win | 69.6728 |
| net_avg_loss | -85.8628 |
| avg_hold_time_bars | 25.2586 |
| exposure | 0.6349 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
