# EMA Hourly Continuation — CWEB/USDT P55_144

**Symbol:** CWEB/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 365 |
| net_profit_factor | 0.5633 |
| net_win_rate | 0.4411 |
| gross_profit_factor | 0.9007 |
| gross_win_rate | 0.4466 |
| sharpe_ratio | -4.1070 |
| sortino_ratio | -1.1052 |
| max_drawdown | 0.7632 |
| cagr | -0.4189 |
| net_avg_win | 59.6078 |
| net_avg_loss | -83.5210 |
| avg_hold_time_bars | 18.4630 |
| exposure | 0.3063 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
