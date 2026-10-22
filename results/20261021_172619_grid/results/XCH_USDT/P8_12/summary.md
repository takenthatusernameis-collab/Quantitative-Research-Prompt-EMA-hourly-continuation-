# EMA Hourly Continuation — XCH/USDT P8_12

**Symbol:** XCH/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 241 |
| net_profit_factor | 0.6150 |
| net_win_rate | 0.4606 |
| gross_profit_factor | 0.8589 |
| gross_win_rate | 0.4606 |
| sharpe_ratio | -2.3440 |
| sortino_ratio | -0.5197 |
| max_drawdown | 0.4593 |
| cagr | -0.2120 |
| net_avg_win | 64.8114 |
| net_avg_loss | -89.9749 |
| avg_hold_time_bars | 4.8548 |
| exposure | 0.0532 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
