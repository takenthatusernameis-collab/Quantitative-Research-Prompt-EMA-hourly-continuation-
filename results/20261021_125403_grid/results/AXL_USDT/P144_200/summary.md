# EMA Hourly Continuation — AXL/USDT P144_200

**Symbol:** AXL/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 251 |
| net_profit_factor | 0.6804 |
| net_win_rate | 0.4661 |
| gross_profit_factor | 0.8905 |
| gross_win_rate | 0.4661 |
| sharpe_ratio | -2.0366 |
| sortino_ratio | -0.4591 |
| max_drawdown | 0.4612 |
| cagr | -0.1907 |
| net_avg_win | 75.2376 |
| net_avg_loss | -96.5521 |
| avg_hold_time_bars | 6.9602 |
| exposure | 0.0791 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
