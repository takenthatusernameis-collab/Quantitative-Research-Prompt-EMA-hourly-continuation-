# EMA Hourly Continuation — FLR/USDT P20_34

**Symbol:** FLR/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 349 |
| net_profit_factor | 0.5050 |
| net_win_rate | 0.4155 |
| gross_profit_factor | 0.7415 |
| gross_win_rate | 0.4155 |
| sharpe_ratio | -4.2856 |
| sortino_ratio | -1.1452 |
| max_drawdown | 0.7490 |
| cagr | -0.4108 |
| net_avg_win | 51.7213 |
| net_avg_loss | -72.7966 |
| avg_hold_time_bars | 5.1834 |
| exposure | 0.0822 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
