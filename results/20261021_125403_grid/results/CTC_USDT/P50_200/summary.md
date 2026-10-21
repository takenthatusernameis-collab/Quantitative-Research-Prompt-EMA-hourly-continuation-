# EMA Hourly Continuation — CTC/USDT P50_200

**Symbol:** CTC/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 323 |
| net_profit_factor | 0.7727 |
| net_win_rate | 0.5046 |
| gross_profit_factor | 0.9961 |
| gross_win_rate | 0.5046 |
| sharpe_ratio | -1.3465 |
| sortino_ratio | -0.3466 |
| max_drawdown | 0.3912 |
| cagr | -0.1483 |
| net_avg_win | 69.1679 |
| net_avg_loss | -91.1941 |
| avg_hold_time_bars | 23.3560 |
| exposure | 0.3429 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
