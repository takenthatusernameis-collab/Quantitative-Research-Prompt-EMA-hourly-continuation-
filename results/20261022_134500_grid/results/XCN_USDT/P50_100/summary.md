# EMA Hourly Continuation — XCN/USDT P50_100

**Symbol:** XCN/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 805 |
| net_profit_factor | 0.3927 |
| net_win_rate | 0.3888 |
| gross_profit_factor | 0.7888 |
| gross_win_rate | 0.4062 |
| sharpe_ratio | -9.2043 |
| sortino_ratio | -3.6703 |
| max_drawdown | 0.9918 |
| cagr | -0.8509 |
| net_avg_win | 20.4817 |
| net_avg_loss | -33.1843 |
| avg_hold_time_bars | 4.9640 |
| exposure | 0.1816 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
