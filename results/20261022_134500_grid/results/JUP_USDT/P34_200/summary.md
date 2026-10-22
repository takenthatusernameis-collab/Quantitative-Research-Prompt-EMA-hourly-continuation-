# EMA Hourly Continuation — JUP/USDT P34_200

**Symbol:** JUP/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 448 |
| net_profit_factor | 0.6159 |
| net_win_rate | 0.4531 |
| gross_profit_factor | 0.8537 |
| gross_win_rate | 0.4531 |
| sharpe_ratio | -3.5354 |
| sortino_ratio | -1.0441 |
| max_drawdown | 0.7389 |
| cagr | -0.3985 |
| net_avg_win | 56.9661 |
| net_avg_loss | -76.6306 |
| avg_hold_time_bars | 21.7478 |
| exposure | 0.4429 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
