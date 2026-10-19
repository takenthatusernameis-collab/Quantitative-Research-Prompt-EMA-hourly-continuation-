# EMA Hourly Continuation — BAT/USDT P8_26

**Symbol:** BAT/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1453 |
| net_profit_factor | 0.3198 |
| net_win_rate | 0.4384 |
| gross_profit_factor | 0.7684 |
| gross_win_rate | 0.4666 |
| sharpe_ratio | -10.1977 |
| sortino_ratio | -5.4668 |
| max_drawdown | 0.9990 |
| cagr | -0.9345 |
| net_avg_win | 7.3719 |
| net_avg_loss | -17.9967 |
| avg_hold_time_bars | 4.3730 |
| exposure | 0.2888 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
