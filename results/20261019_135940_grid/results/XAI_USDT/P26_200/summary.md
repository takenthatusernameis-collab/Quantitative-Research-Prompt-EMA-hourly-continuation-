# EMA Hourly Continuation — XAI/USDT P26_200

**Symbol:** XAI/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 312 |
| net_profit_factor | 0.7989 |
| net_win_rate | 0.5064 |
| gross_profit_factor | 1.0622 |
| gross_win_rate | 0.5096 |
| sharpe_ratio | -1.4336 |
| sortino_ratio | -0.3562 |
| max_drawdown | 0.4739 |
| cagr | -0.1579 |
| net_avg_win | 88.1540 |
| net_avg_loss | -113.2038 |
| avg_hold_time_bars | 46.9776 |
| exposure | 0.6662 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
