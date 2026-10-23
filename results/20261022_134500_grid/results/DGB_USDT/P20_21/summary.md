# EMA Hourly Continuation — DGB/USDT P20_21

**Symbol:** DGB/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1349 |
| net_profit_factor | 0.1522 |
| net_win_rate | 0.2617 |
| gross_profit_factor | 0.6513 |
| gross_win_rate | 0.3336 |
| sharpe_ratio | -20.1381 |
| sortino_ratio | -11.4575 |
| max_drawdown | 1.0000 |
| cagr | -0.9983 |
| net_avg_win | 5.0843 |
| net_avg_loss | -11.8421 |
| avg_hold_time_bars | 1.7658 |
| exposure | 0.1083 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
