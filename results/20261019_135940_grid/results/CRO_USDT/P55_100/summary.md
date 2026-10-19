# EMA Hourly Continuation — CRO/USDT P55_100

**Symbol:** CRO/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 644 |
| net_profit_factor | 0.4009 |
| net_win_rate | 0.4270 |
| gross_profit_factor | 0.9188 |
| gross_win_rate | 0.4674 |
| sharpe_ratio | -7.3007 |
| sortino_ratio | -2.6223 |
| max_drawdown | 0.9651 |
| cagr | -0.7344 |
| net_avg_win | 23.4635 |
| net_avg_loss | -43.6163 |
| avg_hold_time_bars | 5.3292 |
| exposure | 0.1560 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
