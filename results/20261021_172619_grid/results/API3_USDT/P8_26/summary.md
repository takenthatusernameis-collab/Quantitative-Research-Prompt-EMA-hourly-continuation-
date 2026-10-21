# EMA Hourly Continuation — API3/USDT P8_26

**Symbol:** API3/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 707 |
| net_profit_factor | 0.6511 |
| net_win_rate | 0.4639 |
| gross_profit_factor | 0.8646 |
| gross_win_rate | 0.4639 |
| sharpe_ratio | -3.7705 |
| sortino_ratio | -1.4292 |
| max_drawdown | 0.8089 |
| cagr | -0.4807 |
| net_avg_win | 45.9289 |
| net_avg_loss | -61.0445 |
| avg_hold_time_bars | 7.8402 |
| exposure | 0.2520 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
