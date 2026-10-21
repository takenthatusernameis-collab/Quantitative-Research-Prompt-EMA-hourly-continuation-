# EMA Hourly Continuation — YFI/USDT P26_55

**Symbol:** YFI/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 558 |
| net_profit_factor | 0.5814 |
| net_win_rate | 0.4749 |
| gross_profit_factor | 0.9182 |
| gross_win_rate | 0.4749 |
| sharpe_ratio | -4.0906 |
| sortino_ratio | -1.3864 |
| max_drawdown | 0.8072 |
| cagr | -0.4687 |
| net_avg_win | 41.7774 |
| net_avg_loss | -64.9921 |
| avg_hold_time_bars | 6.2652 |
| exposure | 0.1582 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
