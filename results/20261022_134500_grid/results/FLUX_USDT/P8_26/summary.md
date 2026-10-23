# EMA Hourly Continuation — FLUX/USDT P8_26

**Symbol:** FLUX/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1556 |
| net_profit_factor | 0.4885 |
| net_win_rate | 0.4608 |
| gross_profit_factor | 0.9206 |
| gross_win_rate | 0.4743 |
| sharpe_ratio | -9.1050 |
| sortino_ratio | -5.0610 |
| max_drawdown | 0.9981 |
| cagr | -0.9171 |
| net_avg_win | 13.2924 |
| net_avg_loss | -23.2556 |
| avg_hold_time_bars | 3.6594 |
| exposure | 0.2588 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
