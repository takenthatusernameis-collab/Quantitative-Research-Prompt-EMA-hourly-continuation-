# EMA Hourly Continuation — IOST/USDT P20_34

**Symbol:** IOST/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1100 |
| net_profit_factor | 0.2905 |
| net_win_rate | 0.4082 |
| gross_profit_factor | 0.8054 |
| gross_win_rate | 0.4482 |
| sharpe_ratio | -11.2677 |
| sortino_ratio | -5.3286 |
| max_drawdown | 0.9990 |
| cagr | -0.9365 |
| net_avg_win | 9.1098 |
| net_avg_loss | -21.6289 |
| avg_hold_time_bars | 3.1918 |
| exposure | 0.1596 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
