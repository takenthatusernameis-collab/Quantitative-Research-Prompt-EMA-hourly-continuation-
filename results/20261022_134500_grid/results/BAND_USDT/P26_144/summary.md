# EMA Hourly Continuation — BAND/USDT P26_144

**Symbol:** BAND/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 502 |
| net_profit_factor | 0.6640 |
| net_win_rate | 0.4781 |
| gross_profit_factor | 0.9381 |
| gross_win_rate | 0.4880 |
| sharpe_ratio | -2.8681 |
| sortino_ratio | -0.9122 |
| max_drawdown | 0.6723 |
| cagr | -0.3438 |
| net_avg_win | 53.8880 |
| net_avg_loss | -74.3435 |
| avg_hold_time_bars | 19.2948 |
| exposure | 0.4383 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
