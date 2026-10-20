# EMA Hourly Continuation — XCH/USDT P55_100

**Symbol:** XCH/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 708 |
| net_profit_factor | 0.3221 |
| net_win_rate | 0.4138 |
| gross_profit_factor | 0.6624 |
| gross_win_rate | 0.4223 |
| sharpe_ratio | -7.5169 |
| sortino_ratio | -2.8086 |
| max_drawdown | 0.9721 |
| cagr | -0.7594 |
| net_avg_win | 15.7652 |
| net_avg_loss | -34.5538 |
| avg_hold_time_bars | 5.1172 |
| exposure | 0.1647 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
