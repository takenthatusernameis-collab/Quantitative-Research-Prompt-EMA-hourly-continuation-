# EMA Hourly Continuation — ATOM/USDT P55_100

**Symbol:** ATOM/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 574 |
| net_profit_factor | 0.5007 |
| net_win_rate | 0.5017 |
| gross_profit_factor | 0.9633 |
| gross_win_rate | 0.5122 |
| sharpe_ratio | -4.3793 |
| sortino_ratio | -1.4763 |
| max_drawdown | 0.8432 |
| cagr | -0.5146 |
| net_avg_win | 29.1525 |
| net_avg_loss | -58.6292 |
| avg_hold_time_bars | 5.0819 |
| exposure | 0.1326 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
