# EMA Hourly Continuation — GMX/USDT P12_55

**Symbol:** GMX/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 998 |
| net_profit_factor | 0.4997 |
| net_win_rate | 0.4208 |
| gross_profit_factor | 0.7949 |
| gross_win_rate | 0.4319 |
| sharpe_ratio | -7.3386 |
| sortino_ratio | -3.2585 |
| max_drawdown | 0.9814 |
| cagr | -0.7936 |
| net_avg_win | 23.3299 |
| net_avg_loss | -33.9245 |
| avg_hold_time_bars | 8.7886 |
| exposure | 0.3987 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
