# EMA Hourly Continuation — GRAM/USDT P34_100

**Symbol:** GRAM/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 712 |
| net_profit_factor | 0.4051 |
| net_win_rate | 0.4284 |
| gross_profit_factor | 0.8641 |
| gross_win_rate | 0.4508 |
| sharpe_ratio | -7.1029 |
| sortino_ratio | -2.6555 |
| max_drawdown | 0.9675 |
| cagr | -0.7365 |
| net_avg_win | 21.5404 |
| net_avg_loss | -39.8498 |
| avg_hold_time_bars | 8.5154 |
| exposure | 0.2756 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
