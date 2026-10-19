# EMA Hourly Continuation — UNI/USDT P26_55

**Symbol:** UNI/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 931 |
| net_profit_factor | 0.4675 |
| net_win_rate | 0.4468 |
| gross_profit_factor | 0.8543 |
| gross_win_rate | 0.4554 |
| sharpe_ratio | -7.4346 |
| sortino_ratio | -3.1825 |
| max_drawdown | 0.9819 |
| cagr | -0.7953 |
| net_avg_win | 20.7101 |
| net_avg_loss | -35.7847 |
| avg_hold_time_bars | 4.2492 |
| exposure | 0.1798 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
