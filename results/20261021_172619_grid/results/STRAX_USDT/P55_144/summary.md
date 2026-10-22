# EMA Hourly Continuation — STRAX/USDT P55_144

**Symbol:** STRAX/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 390 |
| net_profit_factor | 0.6109 |
| net_win_rate | 0.4410 |
| gross_profit_factor | 0.8380 |
| gross_win_rate | 0.4410 |
| sharpe_ratio | -3.4508 |
| sortino_ratio | -0.9694 |
| max_drawdown | 0.6730 |
| cagr | -0.3609 |
| net_avg_win | 61.4293 |
| net_avg_loss | -79.3393 |
| avg_hold_time_bars | 13.1103 |
| exposure | 0.2338 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
