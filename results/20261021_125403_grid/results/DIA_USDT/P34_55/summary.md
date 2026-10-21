# EMA Hourly Continuation — DIA/USDT P34_55

**Symbol:** DIA/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 404 |
| net_profit_factor | 0.5544 |
| net_win_rate | 0.4356 |
| gross_profit_factor | 0.7926 |
| gross_win_rate | 0.4381 |
| sharpe_ratio | -3.8468 |
| sortino_ratio | -1.1007 |
| max_drawdown | 0.7331 |
| cagr | -0.3965 |
| net_avg_win | 50.9199 |
| net_avg_loss | -70.8983 |
| avg_hold_time_bars | 6.1881 |
| exposure | 0.1131 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
