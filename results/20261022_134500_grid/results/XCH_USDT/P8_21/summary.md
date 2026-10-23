# EMA Hourly Continuation — XCH/USDT P8_21

**Symbol:** XCH/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1943 |
| net_profit_factor | 0.2202 |
| net_win_rate | 0.3906 |
| gross_profit_factor | 0.6798 |
| gross_win_rate | 0.4092 |
| sharpe_ratio | -15.1828 |
| sortino_ratio | -9.4875 |
| max_drawdown | 1.0000 |
| cagr | -0.9921 |
| net_avg_win | 3.7210 |
| net_avg_loss | -10.8312 |
| avg_hold_time_bars | 2.6727 |
| exposure | 0.2360 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
