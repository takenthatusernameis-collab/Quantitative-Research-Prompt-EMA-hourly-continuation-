# EMA Hourly Continuation — XCN/USDT P8_89

**Symbol:** XCN/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 568 |
| net_profit_factor | 0.7826 |
| net_win_rate | 0.4930 |
| gross_profit_factor | 0.9671 |
| gross_win_rate | 0.4930 |
| sharpe_ratio | -1.8624 |
| sortino_ratio | -0.6339 |
| max_drawdown | 0.5333 |
| cagr | -0.2551 |
| net_avg_win | 67.2059 |
| net_avg_loss | -83.4858 |
| avg_hold_time_bars | 20.5000 |
| exposure | 0.5293 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
