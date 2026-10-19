# EMA Hourly Continuation — SUN/USDT P12_55

**Symbol:** SUN/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 889 |
| net_profit_factor | 0.3381 |
| net_win_rate | 0.3903 |
| gross_profit_factor | 0.8932 |
| gross_win_rate | 0.4364 |
| sharpe_ratio | -10.4792 |
| sortino_ratio | -4.4279 |
| max_drawdown | 0.9972 |
| cagr | -0.9032 |
| net_avg_win | 14.6828 |
| net_avg_loss | -27.7994 |
| avg_hold_time_bars | 10.3150 |
| exposure | 0.4150 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
