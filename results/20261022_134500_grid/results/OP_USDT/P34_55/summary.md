# EMA Hourly Continuation — OP/USDT P34_55

**Symbol:** OP/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 898 |
| net_profit_factor | 0.4472 |
| net_win_rate | 0.4644 |
| gross_profit_factor | 0.9278 |
| gross_win_rate | 0.4744 |
| sharpe_ratio | -7.2056 |
| sortino_ratio | -3.0574 |
| max_drawdown | 0.9781 |
| cagr | -0.7768 |
| net_avg_win | 18.9474 |
| net_avg_loss | -36.7352 |
| avg_hold_time_bars | 3.0824 |
| exposure | 0.1258 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
