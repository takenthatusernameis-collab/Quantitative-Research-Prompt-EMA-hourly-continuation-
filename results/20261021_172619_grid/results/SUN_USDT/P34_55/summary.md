# EMA Hourly Continuation — SUN/USDT P34_55

**Symbol:** SUN/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 382 |
| net_profit_factor | 0.3675 |
| net_win_rate | 0.3953 |
| gross_profit_factor | 0.8100 |
| gross_win_rate | 0.4267 |
| sharpe_ratio | -6.6491 |
| sortino_ratio | -1.8955 |
| max_drawdown | 0.9061 |
| cagr | -0.6037 |
| net_avg_win | 34.7553 |
| net_avg_loss | -61.8171 |
| avg_hold_time_bars | 6.3848 |
| exposure | 0.1104 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
