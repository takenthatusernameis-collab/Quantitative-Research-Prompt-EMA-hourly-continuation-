# EMA Hourly Continuation — FIL/USDT P21_55

**Symbol:** FIL/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 951 |
| net_profit_factor | 0.4434 |
| net_win_rate | 0.4532 |
| gross_profit_factor | 0.8163 |
| gross_win_rate | 0.4637 |
| sharpe_ratio | -7.1746 |
| sortino_ratio | -3.1079 |
| max_drawdown | 0.9791 |
| cagr | -0.7837 |
| net_avg_win | 18.0895 |
| net_avg_loss | -33.8127 |
| avg_hold_time_bars | 4.7592 |
| exposure | 0.2057 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
