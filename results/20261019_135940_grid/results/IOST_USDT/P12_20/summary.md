# EMA Hourly Continuation — IOST/USDT P12_20

**Symbol:** IOST/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1423 |
| net_profit_factor | 0.2373 |
| net_win_rate | 0.3893 |
| gross_profit_factor | 0.7763 |
| gross_win_rate | 0.4469 |
| sharpe_ratio | -13.9266 |
| sortino_ratio | -7.5681 |
| max_drawdown | 0.9999 |
| cagr | -0.9802 |
| net_avg_win | 5.6165 |
| net_avg_loss | -15.0875 |
| avg_hold_time_bars | 3.0162 |
| exposure | 0.1951 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
