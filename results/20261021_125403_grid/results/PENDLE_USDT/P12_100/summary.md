# EMA Hourly Continuation — PENDLE/USDT P12_100

**Symbol:** PENDLE/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 441 |
| net_profit_factor | 0.7776 |
| net_win_rate | 0.4807 |
| gross_profit_factor | 0.9128 |
| gross_win_rate | 0.4807 |
| sharpe_ratio | -1.5930 |
| sortino_ratio | -0.4766 |
| max_drawdown | 0.4734 |
| cagr | -0.1979 |
| net_avg_win | 70.1439 |
| net_avg_loss | -83.5063 |
| avg_hold_time_bars | 28.8617 |
| exposure | 0.5785 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
