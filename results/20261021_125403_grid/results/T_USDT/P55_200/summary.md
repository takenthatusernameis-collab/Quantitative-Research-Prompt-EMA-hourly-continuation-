# EMA Hourly Continuation — T/USDT P55_200

**Symbol:** T/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 291 |
| net_profit_factor | 0.7377 |
| net_win_rate | 0.5017 |
| gross_profit_factor | 0.9902 |
| gross_win_rate | 0.5017 |
| sharpe_ratio | -1.4970 |
| sortino_ratio | -0.3649 |
| max_drawdown | 0.3835 |
| cagr | -0.1536 |
| net_avg_win | 66.1462 |
| net_avg_loss | -90.2812 |
| avg_hold_time_bars | 30.1718 |
| exposure | 0.3973 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
