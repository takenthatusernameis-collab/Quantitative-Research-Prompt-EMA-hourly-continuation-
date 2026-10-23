# EMA Hourly Continuation — YGG/USDT P21_100

**Symbol:** YGG/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 666 |
| net_profit_factor | 0.6955 |
| net_win_rate | 0.4805 |
| gross_profit_factor | 0.9812 |
| gross_win_rate | 0.4910 |
| sharpe_ratio | -3.2567 |
| sortino_ratio | -1.1911 |
| max_drawdown | 0.7642 |
| cagr | -0.4252 |
| net_avg_win | 53.7113 |
| net_avg_loss | -71.4260 |
| avg_hold_time_bars | 13.6622 |
| exposure | 0.4117 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
