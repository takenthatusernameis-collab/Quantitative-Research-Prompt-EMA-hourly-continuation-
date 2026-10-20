# EMA Hourly Continuation — PUNDIX/USDT P12_20

**Symbol:** PUNDIX/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1383 |
| net_profit_factor | 0.2385 |
| net_win_rate | 0.3774 |
| gross_profit_factor | 0.6581 |
| gross_win_rate | 0.4252 |
| sharpe_ratio | -14.2081 |
| sortino_ratio | -7.6339 |
| max_drawdown | 0.9999 |
| cagr | -0.9800 |
| net_avg_win | 5.9994 |
| net_avg_loss | -15.2510 |
| avg_hold_time_bars | 3.2082 |
| exposure | 0.2017 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
