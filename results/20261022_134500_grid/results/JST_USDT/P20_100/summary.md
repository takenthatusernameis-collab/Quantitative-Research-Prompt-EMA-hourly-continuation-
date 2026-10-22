# EMA Hourly Continuation — JST/USDT P20_100

**Symbol:** JST/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 594 |
| net_profit_factor | 0.4032 |
| net_win_rate | 0.4747 |
| gross_profit_factor | 1.0554 |
| gross_win_rate | 0.5084 |
| sharpe_ratio | -5.5798 |
| sortino_ratio | -1.8822 |
| max_drawdown | 0.9221 |
| cagr | -0.6225 |
| net_avg_win | 21.9084 |
| net_avg_loss | -49.1087 |
| avg_hold_time_bars | 15.9428 |
| exposure | 0.4285 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
