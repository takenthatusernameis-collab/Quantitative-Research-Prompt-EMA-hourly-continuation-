# EMA Hourly Continuation — MOCA/USDT P50_55

**Symbol:** MOCA/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 696 |
| net_profit_factor | 0.2647 |
| net_win_rate | 0.3463 |
| gross_profit_factor | 0.7114 |
| gross_win_rate | 0.4037 |
| sharpe_ratio | -11.8440 |
| sortino_ratio | -4.8018 |
| max_drawdown | 0.9974 |
| cagr | -0.9264 |
| net_avg_win | 14.8944 |
| net_avg_loss | -29.8094 |
| avg_hold_time_bars | 2.0532 |
| exposure | 0.0716 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
