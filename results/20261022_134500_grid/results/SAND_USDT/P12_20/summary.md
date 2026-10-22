# EMA Hourly Continuation — SAND/USDT P12_20

**Symbol:** SAND/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1471 |
| net_profit_factor | 0.2243 |
| net_win_rate | 0.3780 |
| gross_profit_factor | 0.7949 |
| gross_win_rate | 0.4222 |
| sharpe_ratio | -15.0094 |
| sortino_ratio | -8.2764 |
| max_drawdown | 1.0000 |
| cagr | -0.9874 |
| net_avg_win | 5.2005 |
| net_avg_loss | -14.0889 |
| avg_hold_time_bars | 2.0945 |
| exposure | 0.1400 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
