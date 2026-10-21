# EMA Hourly Continuation — OP/USDT P26_55

**Symbol:** OP/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 444 |
| net_profit_factor | 0.7125 |
| net_win_rate | 0.4932 |
| gross_profit_factor | 0.9491 |
| gross_win_rate | 0.4932 |
| sharpe_ratio | -2.0920 |
| sortino_ratio | -0.6313 |
| max_drawdown | 0.5226 |
| cagr | -0.2508 |
| net_avg_win | 58.3417 |
| net_avg_loss | -79.7051 |
| avg_hold_time_bars | 6.6014 |
| exposure | 0.1332 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
