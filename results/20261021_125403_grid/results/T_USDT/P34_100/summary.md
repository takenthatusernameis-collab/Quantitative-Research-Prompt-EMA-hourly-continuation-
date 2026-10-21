# EMA Hourly Continuation — T/USDT P34_100

**Symbol:** T/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 451 |
| net_profit_factor | 0.7063 |
| net_win_rate | 0.4922 |
| gross_profit_factor | 0.9847 |
| gross_win_rate | 0.4945 |
| sharpe_ratio | -2.4160 |
| sortino_ratio | -0.7324 |
| max_drawdown | 0.5861 |
| cagr | -0.2849 |
| net_avg_win | 61.8351 |
| net_avg_loss | -84.8742 |
| avg_hold_time_bars | 13.6563 |
| exposure | 0.2787 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
