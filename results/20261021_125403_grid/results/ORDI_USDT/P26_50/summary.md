# EMA Hourly Continuation — ORDI/USDT P26_50

**Symbol:** ORDI/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 412 |
| net_profit_factor | 0.7066 |
| net_win_rate | 0.4709 |
| gross_profit_factor | 0.9244 |
| gross_win_rate | 0.4709 |
| sharpe_ratio | -2.4755 |
| sortino_ratio | -0.7170 |
| max_drawdown | 0.5619 |
| cagr | -0.2801 |
| net_avg_win | 69.7654 |
| net_avg_loss | -87.8623 |
| avg_hold_time_bars | 5.9248 |
| exposure | 0.1110 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
