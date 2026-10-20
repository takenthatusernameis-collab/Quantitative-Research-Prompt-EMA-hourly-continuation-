# EMA Hourly Continuation — YGG/USDT P20_100

**Symbol:** YGG/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 652 |
| net_profit_factor | 0.6909 |
| net_win_rate | 0.4785 |
| gross_profit_factor | 0.9790 |
| gross_win_rate | 0.4893 |
| sharpe_ratio | -3.2931 |
| sortino_ratio | -1.1905 |
| max_drawdown | 0.7651 |
| cagr | -0.4260 |
| net_avg_win | 53.9755 |
| net_avg_loss | -71.6911 |
| avg_hold_time_bars | 14.6135 |
| exposure | 0.4312 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
