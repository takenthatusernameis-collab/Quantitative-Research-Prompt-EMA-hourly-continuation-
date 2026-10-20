# EMA Hourly Continuation — XCH/USDT P50_100

**Symbol:** XCH/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 705 |
| net_profit_factor | 0.3815 |
| net_win_rate | 0.4340 |
| gross_profit_factor | 0.7383 |
| gross_win_rate | 0.4397 |
| sharpe_ratio | -6.5466 |
| sortino_ratio | -2.4307 |
| max_drawdown | 0.9536 |
| cagr | -0.7047 |
| net_avg_win | 19.2133 |
| net_avg_loss | -38.6259 |
| avg_hold_time_bars | 6.2227 |
| exposure | 0.1994 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
