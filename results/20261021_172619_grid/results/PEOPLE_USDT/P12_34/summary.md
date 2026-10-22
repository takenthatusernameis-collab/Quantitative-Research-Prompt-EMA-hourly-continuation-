# EMA Hourly Continuation — PEOPLE/USDT P12_34

**Symbol:** PEOPLE/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 652 |
| net_profit_factor | 0.6919 |
| net_win_rate | 0.4617 |
| gross_profit_factor | 0.8884 |
| gross_win_rate | 0.4617 |
| sharpe_ratio | -3.3889 |
| sortino_ratio | -1.2292 |
| max_drawdown | 0.7589 |
| cagr | -0.4311 |
| net_avg_win | 56.6138 |
| net_avg_loss | -70.1710 |
| avg_hold_time_bars | 6.5215 |
| exposure | 0.1924 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
