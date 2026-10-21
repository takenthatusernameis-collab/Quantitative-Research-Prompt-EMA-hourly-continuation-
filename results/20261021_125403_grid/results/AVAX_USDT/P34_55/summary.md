# EMA Hourly Continuation — AVAX/USDT P34_55

**Symbol:** AVAX/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 284 |
| net_profit_factor | 0.6412 |
| net_win_rate | 0.4754 |
| gross_profit_factor | 0.9103 |
| gross_win_rate | 0.4754 |
| sharpe_ratio | -2.3707 |
| sortino_ratio | -0.5724 |
| max_drawdown | 0.5044 |
| cagr | -0.2297 |
| net_avg_win | 63.6363 |
| net_avg_loss | -89.9205 |
| avg_hold_time_bars | 5.8908 |
| exposure | 0.0760 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
