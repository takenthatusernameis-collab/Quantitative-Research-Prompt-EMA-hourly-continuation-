# EMA Hourly Continuation — XCH/USDT P100_200

**Symbol:** XCH/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 442 |
| net_profit_factor | 0.5686 |
| net_win_rate | 0.4661 |
| gross_profit_factor | 0.9382 |
| gross_win_rate | 0.4683 |
| sharpe_ratio | -3.8735 |
| sortino_ratio | -1.1490 |
| max_drawdown | 0.7505 |
| cagr | -0.4247 |
| net_avg_win | 48.0121 |
| net_avg_loss | -73.7093 |
| avg_hold_time_bars | 8.1991 |
| exposure | 0.1647 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
