# EMA Hourly Continuation — XCN/USDT P12_144

**Symbol:** XCN/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 435 |
| net_profit_factor | 0.6834 |
| net_win_rate | 0.4598 |
| gross_profit_factor | 0.8368 |
| gross_win_rate | 0.4621 |
| sharpe_ratio | -2.4070 |
| sortino_ratio | -0.7121 |
| max_drawdown | 0.5687 |
| cagr | -0.2793 |
| net_avg_win | 60.5128 |
| net_avg_loss | -75.3571 |
| avg_hold_time_bars | 29.7563 |
| exposure | 0.5884 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
