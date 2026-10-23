# EMA Hourly Continuation — ANYONE/USDT P21_55

**Symbol:** ANYONE/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 798 |
| net_profit_factor | 0.4911 |
| net_win_rate | 0.4060 |
| gross_profit_factor | 0.6884 |
| gross_win_rate | 0.4098 |
| sharpe_ratio | -6.8410 |
| sortino_ratio | -2.8468 |
| max_drawdown | 0.9564 |
| cagr | -0.7488 |
| net_avg_win | 28.4688 |
| net_avg_loss | -39.6258 |
| avg_hold_time_bars | 5.6404 |
| exposure | 0.2274 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
