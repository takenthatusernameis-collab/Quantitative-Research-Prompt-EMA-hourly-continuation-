# EMA Hourly Continuation — XCH/USDT P26_100

**Symbol:** XCH/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 757 |
| net_profit_factor | 0.5335 |
| net_win_rate | 0.4716 |
| gross_profit_factor | 0.9082 |
| gross_win_rate | 0.4782 |
| sharpe_ratio | -4.7207 |
| sortino_ratio | -1.8126 |
| max_drawdown | 0.8935 |
| cagr | -0.5882 |
| net_avg_win | 28.5765 |
| net_avg_loss | -47.8105 |
| avg_hold_time_bars | 11.0819 |
| exposure | 0.3813 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
