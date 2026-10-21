# EMA Hourly Continuation — PUNDIX/USDT P21_26

**Symbol:** PUNDIX/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 336 |
| net_profit_factor | 0.5021 |
| net_win_rate | 0.4613 |
| gross_profit_factor | 0.8365 |
| gross_win_rate | 0.4643 |
| sharpe_ratio | -3.7708 |
| sortino_ratio | -0.9954 |
| max_drawdown | 0.6869 |
| cagr | -0.3663 |
| net_avg_win | 44.3685 |
| net_avg_loss | -75.6760 |
| avg_hold_time_bars | 5.2589 |
| exposure | 0.0803 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
