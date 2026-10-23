# EMA Hourly Continuation — CWEB/USDT P20_50

**Symbol:** CWEB/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 899 |
| net_profit_factor | 0.3580 |
| net_win_rate | 0.3137 |
| gross_profit_factor | 0.7114 |
| gross_win_rate | 0.3293 |
| sharpe_ratio | -13.1545 |
| sortino_ratio | -5.6851 |
| max_drawdown | 0.9996 |
| cagr | -0.9561 |
| net_avg_win | 19.7631 |
| net_avg_loss | -25.2338 |
| avg_hold_time_bars | 6.3415 |
| exposure | 0.2591 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
