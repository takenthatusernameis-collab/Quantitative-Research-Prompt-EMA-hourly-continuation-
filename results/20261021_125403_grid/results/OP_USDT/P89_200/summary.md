# EMA Hourly Continuation — OP/USDT P89_200

**Symbol:** OP/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 275 |
| net_profit_factor | 0.9492 |
| net_win_rate | 0.5455 |
| gross_profit_factor | 1.1912 |
| gross_win_rate | 0.5455 |
| sharpe_ratio | -0.2387 |
| sortino_ratio | -0.0574 |
| max_drawdown | 0.1918 |
| cagr | -0.0300 |
| net_avg_win | 91.7012 |
| net_avg_loss | -115.9253 |
| avg_hold_time_bars | 14.0800 |
| exposure | 0.1760 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
