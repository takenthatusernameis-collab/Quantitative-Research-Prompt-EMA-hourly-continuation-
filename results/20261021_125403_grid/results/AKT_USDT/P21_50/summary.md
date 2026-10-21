# EMA Hourly Continuation — AKT/USDT P21_50

**Symbol:** AKT/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 459 |
| net_profit_factor | 0.7458 |
| net_win_rate | 0.4924 |
| gross_profit_factor | 0.9548 |
| gross_win_rate | 0.4924 |
| sharpe_ratio | -1.8708 |
| sortino_ratio | -0.5738 |
| max_drawdown | 0.5016 |
| cagr | -0.2312 |
| net_avg_win | 62.7264 |
| net_avg_loss | -81.5812 |
| avg_hold_time_bars | 7.6035 |
| exposure | 0.1586 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
