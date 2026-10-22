# EMA Hourly Continuation — INJ/USDT P8_100

**Symbol:** INJ/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 626 |
| net_profit_factor | 0.6293 |
| net_win_rate | 0.4553 |
| gross_profit_factor | 0.8726 |
| gross_win_rate | 0.4585 |
| sharpe_ratio | -3.9845 |
| sortino_ratio | -1.3937 |
| max_drawdown | 0.8181 |
| cagr | -0.4891 |
| net_avg_win | 48.5374 |
| net_avg_loss | -64.4617 |
| avg_hold_time_bars | 23.8035 |
| exposure | 0.6773 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
