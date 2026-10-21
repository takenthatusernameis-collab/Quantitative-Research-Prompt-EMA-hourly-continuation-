# EMA Hourly Continuation — UMA/USDT P26_100

**Symbol:** UMA/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 492 |
| net_profit_factor | 0.8239 |
| net_win_rate | 0.5183 |
| gross_profit_factor | 1.0834 |
| gross_win_rate | 0.5183 |
| sharpe_ratio | -1.4359 |
| sortino_ratio | -0.4576 |
| max_drawdown | 0.4548 |
| cagr | -0.1911 |
| net_avg_win | 75.7742 |
| net_avg_loss | -98.9496 |
| avg_hold_time_bars | 15.5020 |
| exposure | 0.3467 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
