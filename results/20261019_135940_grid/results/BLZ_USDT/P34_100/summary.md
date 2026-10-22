# EMA Hourly Continuation — BLZ/USDT P34_100

**Symbol:** BLZ/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 692 |
| net_profit_factor | 0.5397 |
| net_win_rate | 0.4032 |
| gross_profit_factor | 0.8210 |
| gross_win_rate | 0.4118 |
| sharpe_ratio | -6.5672 |
| sortino_ratio | -2.4273 |
| max_drawdown | 0.9475 |
| cagr | -0.6869 |
| net_avg_win | 39.7727 |
| net_avg_loss | -49.7868 |
| avg_hold_time_bars | 9.8006 |
| exposure | 0.3069 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
