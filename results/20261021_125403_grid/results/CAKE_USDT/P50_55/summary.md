# EMA Hourly Continuation — CAKE/USDT P50_55

**Symbol:** CAKE/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 99 |
| net_profit_factor | 0.6249 |
| net_win_rate | 0.5051 |
| gross_profit_factor | 1.0212 |
| gross_win_rate | 0.5051 |
| sharpe_ratio | -1.4258 |
| sortino_ratio | -0.2047 |
| max_drawdown | 0.2444 |
| cagr | -0.0889 |
| net_avg_win | 69.4903 |
| net_avg_loss | -113.4701 |
| avg_hold_time_bars | 5.4545 |
| exposure | 0.0245 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
