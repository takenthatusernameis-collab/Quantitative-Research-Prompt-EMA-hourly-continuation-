# EMA Hourly Continuation — GMX/USDT P34_100

**Symbol:** GMX/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 464 |
| net_profit_factor | 0.6646 |
| net_win_rate | 0.4655 |
| gross_profit_factor | 0.8854 |
| gross_win_rate | 0.4655 |
| sharpe_ratio | -2.9039 |
| sortino_ratio | -0.8901 |
| max_drawdown | 0.6520 |
| cagr | -0.3357 |
| net_avg_win | 58.9013 |
| net_avg_loss | -77.1858 |
| avg_hold_time_bars | 12.2823 |
| exposure | 0.2590 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
