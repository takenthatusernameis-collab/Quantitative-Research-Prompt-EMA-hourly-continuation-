# EMA Hourly Continuation — MNT/USDT P12_20

**Symbol:** MNT/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1478 |
| net_profit_factor | 0.1882 |
| net_win_rate | 0.3396 |
| gross_profit_factor | 0.6418 |
| gross_win_rate | 0.4127 |
| sharpe_ratio | -17.0098 |
| sortino_ratio | -9.5497 |
| max_drawdown | 1.0000 |
| cagr | -0.9942 |
| net_avg_win | 4.6190 |
| net_avg_loss | -12.6216 |
| avg_hold_time_bars | 2.6631 |
| exposure | 0.1789 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
