# EMA Hourly Continuation — ZKJ/USDT P21_50

**Symbol:** ZKJ/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1074 |
| net_profit_factor | 0.1788 |
| net_win_rate | 0.2886 |
| gross_profit_factor | 0.4828 |
| gross_win_rate | 0.3613 |
| sharpe_ratio | -15.3980 |
| sortino_ratio | -7.4087 |
| max_drawdown | 1.0000 |
| cagr | -0.9818 |
| net_avg_win | 7.0213 |
| net_avg_loss | -15.9374 |
| avg_hold_time_bars | 7.8473 |
| exposure | 0.3831 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
