# EMA Hourly Continuation — CTC/USDT P8_21

**Symbol:** CTC/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 638 |
| net_profit_factor | 0.6130 |
| net_win_rate | 0.4812 |
| gross_profit_factor | 0.9162 |
| gross_win_rate | 0.4828 |
| sharpe_ratio | -3.6620 |
| sortino_ratio | -1.3257 |
| max_drawdown | 0.7838 |
| cagr | -0.4546 |
| net_avg_win | 40.3414 |
| net_avg_loss | -61.0377 |
| avg_hold_time_bars | 6.4530 |
| exposure | 0.1871 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
