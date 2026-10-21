# EMA Hourly Continuation — JASMY/USDT P8_50

**Symbol:** JASMY/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 701 |
| net_profit_factor | 0.7922 |
| net_win_rate | 0.4950 |
| gross_profit_factor | 0.9721 |
| gross_win_rate | 0.4950 |
| sharpe_ratio | -1.9605 |
| sortino_ratio | -0.7425 |
| max_drawdown | 0.6236 |
| cagr | -0.2905 |
| net_avg_win | 63.4614 |
| net_avg_loss | -78.5219 |
| avg_hold_time_bars | 11.9601 |
| exposure | 0.3811 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
