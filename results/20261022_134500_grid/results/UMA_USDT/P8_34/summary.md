# EMA Hourly Continuation — UMA/USDT P8_34

**Symbol:** UMA/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1342 |
| net_profit_factor | 0.4468 |
| net_win_rate | 0.4374 |
| gross_profit_factor | 0.8423 |
| gross_win_rate | 0.4531 |
| sharpe_ratio | -8.9932 |
| sortino_ratio | -4.6219 |
| max_drawdown | 0.9968 |
| cagr | -0.8978 |
| net_avg_win | 13.7129 |
| net_avg_loss | -23.8635 |
| avg_hold_time_bars | 5.6811 |
| exposure | 0.3465 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
