# EMA Hourly Continuation — KAS/USDT P21_200

**Symbol:** KAS/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 336 |
| net_profit_factor | 0.8410 |
| net_win_rate | 0.5089 |
| gross_profit_factor | 1.0197 |
| gross_win_rate | 0.5089 |
| sharpe_ratio | -0.9469 |
| sortino_ratio | -0.2486 |
| max_drawdown | 0.2662 |
| cagr | -0.1098 |
| net_avg_win | 78.3542 |
| net_avg_loss | -96.5609 |
| avg_hold_time_bars | 36.7262 |
| exposure | 0.5609 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
