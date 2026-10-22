# EMA Hourly Continuation — AKT/USDT P26_200

**Symbol:** AKT/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 425 |
| net_profit_factor | 0.7542 |
| net_win_rate | 0.5106 |
| gross_profit_factor | 1.0255 |
| gross_win_rate | 0.5106 |
| sharpe_ratio | -1.6813 |
| sortino_ratio | -0.4892 |
| max_drawdown | 0.4504 |
| cagr | -0.2091 |
| net_avg_win | 62.9349 |
| net_avg_loss | -87.0594 |
| avg_hold_time_bars | 27.0965 |
| exposure | 0.5235 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
