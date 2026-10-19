# EMA Hourly Continuation — KCS/USDT P8_55

**Symbol:** KCS/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 983 |
| net_profit_factor | 0.2337 |
| net_win_rate | 0.3622 |
| gross_profit_factor | 0.6014 |
| gross_win_rate | 0.4100 |
| sharpe_ratio | -12.1813 |
| sortino_ratio | -5.4630 |
| max_drawdown | 0.9993 |
| cagr | -0.9450 |
| net_avg_win | 8.5609 |
| net_avg_loss | -20.7988 |
| avg_hold_time_bars | 11.5290 |
| exposure | 0.5151 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
