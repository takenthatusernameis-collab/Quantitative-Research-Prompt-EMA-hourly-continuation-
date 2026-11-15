# EMA Hourly Continuation — CERE/USDT P50_55

**Symbol:** CERE/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 842 |
| net_profit_factor | 0.1388 |
| net_win_rate | 0.2399 |
| gross_profit_factor | 0.4829 |
| gross_win_rate | 0.3100 |
| sharpe_ratio | -15.9305 |
| sortino_ratio | -7.1076 |
| max_drawdown | 1.0000 |
| cagr | -0.9814 |
| net_avg_win | 7.9805 |
| net_avg_loss | -18.1431 |
| avg_hold_time_bars | 3.7209 |
| exposure | 0.1424 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
