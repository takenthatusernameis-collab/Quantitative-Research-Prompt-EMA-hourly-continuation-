# EMA Hourly Continuation — SQD/USDT P8_55

**Symbol:** SQD/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1006 |
| net_profit_factor | 0.7119 |
| net_win_rate | 0.4920 |
| gross_profit_factor | 1.0119 |
| gross_win_rate | 0.4980 |
| sharpe_ratio | -3.7618 |
| sortino_ratio | -1.7141 |
| max_drawdown | 0.8695 |
| cagr | -0.5554 |
| net_avg_win | 42.9491 |
| net_avg_loss | -58.4412 |
| avg_hold_time_bars | 9.3072 |
| exposure | 0.4401 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
