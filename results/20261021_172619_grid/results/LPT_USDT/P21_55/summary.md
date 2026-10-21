# EMA Hourly Continuation — LPT/USDT P21_55

**Symbol:** LPT/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 575 |
| net_profit_factor | 0.7296 |
| net_win_rate | 0.4887 |
| gross_profit_factor | 0.9799 |
| gross_win_rate | 0.4904 |
| sharpe_ratio | -2.7124 |
| sortino_ratio | -0.9296 |
| max_drawdown | 0.6805 |
| cagr | -0.3481 |
| net_avg_win | 63.2459 |
| net_avg_loss | -82.8496 |
| avg_hold_time_bars | 7.8452 |
| exposure | 0.2050 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
