# EMA Hourly Continuation — KNC/USDT P21_55

**Symbol:** KNC/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 846 |
| net_profit_factor | 0.5691 |
| net_win_rate | 0.4504 |
| gross_profit_factor | 1.0084 |
| gross_win_rate | 0.4764 |
| sharpe_ratio | -6.6214 |
| sortino_ratio | -2.7249 |
| max_drawdown | 0.9647 |
| cagr | -0.7323 |
| net_avg_win | 33.3990 |
| net_avg_loss | -48.0857 |
| avg_hold_time_bars | 7.2553 |
| exposure | 0.2790 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
