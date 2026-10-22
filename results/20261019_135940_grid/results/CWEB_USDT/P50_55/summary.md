# EMA Hourly Continuation — CWEB/USDT P50_55

**Symbol:** CWEB/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 782 |
| net_profit_factor | 0.1419 |
| net_win_rate | 0.2059 |
| gross_profit_factor | 0.6039 |
| gross_win_rate | 0.2545 |
| sharpe_ratio | -16.8020 |
| sortino_ratio | -7.5272 |
| max_drawdown | 1.0000 |
| cagr | -0.9869 |
| net_avg_win | 10.2734 |
| net_avg_loss | -18.7662 |
| avg_hold_time_bars | 2.8990 |
| exposure | 0.1030 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
