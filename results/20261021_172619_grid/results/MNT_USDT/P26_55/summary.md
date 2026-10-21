# EMA Hourly Continuation — MNT/USDT P26_55

**Symbol:** MNT/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 432 |
| net_profit_factor | 0.5948 |
| net_win_rate | 0.4699 |
| gross_profit_factor | 0.8829 |
| gross_win_rate | 0.4699 |
| sharpe_ratio | -3.3975 |
| sortino_ratio | -1.0102 |
| max_drawdown | 0.6940 |
| cagr | -0.3719 |
| net_avg_win | 49.8193 |
| net_avg_loss | -74.2480 |
| avg_hold_time_bars | 8.5625 |
| exposure | 0.1681 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
