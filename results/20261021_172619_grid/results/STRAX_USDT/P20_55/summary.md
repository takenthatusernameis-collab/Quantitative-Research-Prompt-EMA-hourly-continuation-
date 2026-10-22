# EMA Hourly Continuation — STRAX/USDT P20_55

**Symbol:** STRAX/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 573 |
| net_profit_factor | 0.6155 |
| net_win_rate | 0.4590 |
| gross_profit_factor | 0.8630 |
| gross_win_rate | 0.4590 |
| sharpe_ratio | -3.9774 |
| sortino_ratio | -1.3579 |
| max_drawdown | 0.7951 |
| cagr | -0.4674 |
| net_avg_win | 48.2364 |
| net_avg_loss | -66.4899 |
| avg_hold_time_bars | 10.2059 |
| exposure | 0.2674 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
