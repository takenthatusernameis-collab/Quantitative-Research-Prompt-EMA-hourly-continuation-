# EMA Hourly Continuation — XCH/USDT P20_34

**Symbol:** XCH/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1393 |
| net_profit_factor | 0.2514 |
| net_win_rate | 0.3934 |
| gross_profit_factor | 0.7639 |
| gross_win_rate | 0.4128 |
| sharpe_ratio | -12.8053 |
| sortino_ratio | -6.8115 |
| max_drawdown | 0.9998 |
| cagr | -0.9688 |
| net_avg_win | 6.1272 |
| net_avg_loss | -15.8060 |
| avg_hold_time_bars | 2.4874 |
| exposure | 0.1575 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
