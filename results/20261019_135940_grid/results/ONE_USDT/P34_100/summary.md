# EMA Hourly Continuation — ONE/USDT P34_100

**Symbol:** ONE/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 695 |
| net_profit_factor | 0.6774 |
| net_win_rate | 0.4719 |
| gross_profit_factor | 1.0287 |
| gross_win_rate | 0.4763 |
| sharpe_ratio | -4.4647 |
| sortino_ratio | -1.6526 |
| max_drawdown | 0.8746 |
| cagr | -0.5521 |
| net_avg_win | 55.4910 |
| net_avg_loss | -73.2166 |
| avg_hold_time_bars | 8.7439 |
| exposure | 0.2762 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
