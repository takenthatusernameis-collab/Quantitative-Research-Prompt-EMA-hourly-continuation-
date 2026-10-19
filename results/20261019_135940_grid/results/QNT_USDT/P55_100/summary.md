# EMA Hourly Continuation — QNT/USDT P55_100

**Symbol:** QNT/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 721 |
| net_profit_factor | 0.3903 |
| net_win_rate | 0.4355 |
| gross_profit_factor | 0.8065 |
| gross_win_rate | 0.4521 |
| sharpe_ratio | -7.1917 |
| sortino_ratio | -2.7253 |
| max_drawdown | 0.9677 |
| cagr | -0.7420 |
| net_avg_win | 19.7046 |
| net_avg_loss | -38.9539 |
| avg_hold_time_bars | 4.7864 |
| exposure | 0.1569 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
