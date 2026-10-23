# EMA Hourly Continuation — DGB/USDT P55_200

**Symbol:** DGB/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 423 |
| net_profit_factor | 0.5942 |
| net_win_rate | 0.4563 |
| gross_profit_factor | 0.8490 |
| gross_win_rate | 0.4586 |
| sharpe_ratio | -3.3675 |
| sortino_ratio | -0.9764 |
| max_drawdown | 0.7020 |
| cagr | -0.3712 |
| net_avg_win | 52.2114 |
| net_avg_loss | -73.7274 |
| avg_hold_time_bars | 19.3641 |
| exposure | 0.3723 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
