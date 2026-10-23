# EMA Hourly Continuation — MOG/USDT P21_100

**Symbol:** MOG/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 594 |
| net_profit_factor | 0.6757 |
| net_win_rate | 0.4613 |
| gross_profit_factor | 0.8715 |
| gross_win_rate | 0.4630 |
| sharpe_ratio | -3.5712 |
| sortino_ratio | -1.2843 |
| max_drawdown | 0.7766 |
| cagr | -0.4539 |
| net_avg_win | 57.0876 |
| net_avg_loss | -72.3423 |
| avg_hold_time_bars | 13.9091 |
| exposure | 0.4107 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
