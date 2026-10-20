# EMA Hourly Continuation — MEW/USDT P21_55

**Symbol:** MEW/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 921 |
| net_profit_factor | 0.4934 |
| net_win_rate | 0.4571 |
| gross_profit_factor | 0.7705 |
| gross_win_rate | 0.4625 |
| sharpe_ratio | -6.2171 |
| sortino_ratio | -2.6440 |
| max_drawdown | 0.9614 |
| cagr | -0.7246 |
| net_avg_win | 22.2305 |
| net_avg_loss | -37.9339 |
| avg_hold_time_bars | 5.1759 |
| exposure | 0.2167 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
