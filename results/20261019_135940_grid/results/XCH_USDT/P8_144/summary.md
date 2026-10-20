# EMA Hourly Continuation — XCH/USDT P8_144

**Symbol:** XCH/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 623 |
| net_profit_factor | 0.6386 |
| net_win_rate | 0.4799 |
| gross_profit_factor | 0.9610 |
| gross_win_rate | 0.4912 |
| sharpe_ratio | -3.2182 |
| sortino_ratio | -1.1337 |
| max_drawdown | 0.7457 |
| cagr | -0.4161 |
| net_avg_win | 43.7955 |
| net_avg_loss | -63.2899 |
| avg_hold_time_bars | 25.7223 |
| exposure | 0.7284 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
