# EMA Hourly Continuation — GRAM/USDT P12_34

**Symbol:** GRAM/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 510 |
| net_profit_factor | 0.6464 |
| net_win_rate | 0.4765 |
| gross_profit_factor | 0.9299 |
| gross_win_rate | 0.4765 |
| sharpe_ratio | -3.2093 |
| sortino_ratio | -1.0381 |
| max_drawdown | 0.7149 |
| cagr | -0.3784 |
| net_avg_win | 52.4426 |
| net_avg_loss | -73.8341 |
| avg_hold_time_bars | 6.9941 |
| exposure | 0.1621 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
