# EMA Hourly Continuation — XCH/USDT P20_55

**Symbol:** XCH/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 585 |
| net_profit_factor | 0.5981 |
| net_win_rate | 0.4513 |
| gross_profit_factor | 0.8004 |
| gross_win_rate | 0.4513 |
| sharpe_ratio | -3.5891 |
| sortino_ratio | -1.2353 |
| max_drawdown | 0.7659 |
| cagr | -0.4337 |
| net_avg_win | 42.8527 |
| net_avg_loss | -58.9275 |
| avg_hold_time_bars | 7.7556 |
| exposure | 0.2062 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
