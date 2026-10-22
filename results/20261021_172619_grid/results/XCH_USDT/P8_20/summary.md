# EMA Hourly Continuation — XCH/USDT P8_20

**Symbol:** XCH/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 466 |
| net_profit_factor | 0.6069 |
| net_win_rate | 0.4571 |
| gross_profit_factor | 0.8399 |
| gross_win_rate | 0.4571 |
| sharpe_ratio | -3.2882 |
| sortino_ratio | -1.0128 |
| max_drawdown | 0.6972 |
| cagr | -0.3719 |
| net_avg_win | 49.9254 |
| net_avg_loss | -69.2623 |
| avg_hold_time_bars | 5.0794 |
| exposure | 0.1076 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
