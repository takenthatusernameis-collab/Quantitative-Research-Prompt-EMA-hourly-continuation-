# EMA Hourly Continuation — AVA/USDT P55_100

**Symbol:** AVA/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 640 |
| net_profit_factor | 0.5560 |
| net_win_rate | 0.4953 |
| gross_profit_factor | 0.9847 |
| gross_win_rate | 0.4953 |
| sharpe_ratio | -4.4591 |
| sortino_ratio | -1.5996 |
| max_drawdown | 0.8609 |
| cagr | -0.5347 |
| net_avg_win | 33.7174 |
| net_avg_loss | -59.5180 |
| avg_hold_time_bars | 5.0484 |
| exposure | 0.1469 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
