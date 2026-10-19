# EMA Hourly Continuation — OP/USDT P21_200

**Symbol:** OP/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 338 |
| net_profit_factor | 0.6196 |
| net_win_rate | 0.4527 |
| gross_profit_factor | 0.8534 |
| gross_win_rate | 0.4615 |
| sharpe_ratio | -2.7380 |
| sortino_ratio | -0.7046 |
| max_drawdown | 0.5713 |
| cagr | -0.2856 |
| net_avg_win | 60.7050 |
| net_avg_loss | -81.0318 |
| avg_hold_time_bars | 42.0562 |
| exposure | 0.6461 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
