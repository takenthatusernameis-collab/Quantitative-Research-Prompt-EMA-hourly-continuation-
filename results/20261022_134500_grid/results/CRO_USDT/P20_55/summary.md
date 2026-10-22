# EMA Hourly Continuation — CRO/USDT P20_55

**Symbol:** CRO/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 989 |
| net_profit_factor | 0.3509 |
| net_win_rate | 0.4146 |
| gross_profit_factor | 0.7630 |
| gross_win_rate | 0.4439 |
| sharpe_ratio | -9.4334 |
| sortino_ratio | -4.1873 |
| max_drawdown | 0.9954 |
| cagr | -0.8801 |
| net_avg_win | 13.1225 |
| net_avg_loss | -26.4795 |
| avg_hold_time_bars | 5.7856 |
| exposure | 0.2601 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
