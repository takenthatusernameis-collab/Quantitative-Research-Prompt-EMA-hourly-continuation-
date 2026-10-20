# EMA Hourly Continuation — MOVR/USDT P34_55

**Symbol:** MOVR/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 914 |
| net_profit_factor | 0.3937 |
| net_win_rate | 0.4420 |
| gross_profit_factor | 0.8498 |
| gross_win_rate | 0.4661 |
| sharpe_ratio | -7.8919 |
| sortino_ratio | -3.3766 |
| max_drawdown | 0.9854 |
| cagr | -0.8122 |
| net_avg_win | 15.8309 |
| net_avg_loss | -31.8544 |
| avg_hold_time_bars | 3.0908 |
| exposure | 0.1284 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
