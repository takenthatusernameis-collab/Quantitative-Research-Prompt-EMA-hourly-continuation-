# EMA Hourly Continuation — DOGE/USDT P8_21

**Symbol:** DOGE/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 432 |
| net_profit_factor | 0.6663 |
| net_win_rate | 0.4815 |
| gross_profit_factor | 0.9189 |
| gross_win_rate | 0.4815 |
| sharpe_ratio | -2.6653 |
| sortino_ratio | -0.7933 |
| max_drawdown | 0.6136 |
| cagr | -0.3054 |
| net_avg_win | 57.5463 |
| net_avg_loss | -80.2010 |
| avg_hold_time_bars | 5.7523 |
| exposure | 0.1130 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
