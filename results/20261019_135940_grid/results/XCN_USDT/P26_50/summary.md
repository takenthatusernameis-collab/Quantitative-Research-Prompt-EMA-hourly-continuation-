# EMA Hourly Continuation — XCN/USDT P26_50

**Symbol:** XCN/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1188 |
| net_profit_factor | 0.2698 |
| net_win_rate | 0.3611 |
| gross_profit_factor | 0.6247 |
| gross_win_rate | 0.3880 |
| sharpe_ratio | -12.3894 |
| sortino_ratio | -6.0718 |
| max_drawdown | 0.9996 |
| cagr | -0.9558 |
| net_avg_win | 8.6093 |
| net_avg_loss | -18.0361 |
| avg_hold_time_bars | 3.3392 |
| exposure | 0.1803 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
