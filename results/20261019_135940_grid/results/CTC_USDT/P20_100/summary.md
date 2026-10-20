# EMA Hourly Continuation — CTC/USDT P20_100

**Symbol:** CTC/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 716 |
| net_profit_factor | 0.5639 |
| net_win_rate | 0.4735 |
| gross_profit_factor | 0.9283 |
| gross_win_rate | 0.4888 |
| sharpe_ratio | -4.7814 |
| sortino_ratio | -1.7871 |
| max_drawdown | 0.9020 |
| cagr | -0.5856 |
| net_avg_win | 33.9711 |
| net_avg_loss | -54.1695 |
| avg_hold_time_bars | 12.7542 |
| exposure | 0.4151 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
