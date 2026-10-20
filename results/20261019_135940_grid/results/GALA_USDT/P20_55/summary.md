# EMA Hourly Continuation — GALA/USDT P20_55

**Symbol:** GALA/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1012 |
| net_profit_factor | 0.4747 |
| net_win_rate | 0.4338 |
| gross_profit_factor | 0.7888 |
| gross_win_rate | 0.4407 |
| sharpe_ratio | -7.3881 |
| sortino_ratio | -3.3345 |
| max_drawdown | 0.9827 |
| cagr | -0.7955 |
| net_avg_win | 20.2002 |
| net_avg_loss | -32.6042 |
| avg_hold_time_bars | 4.9555 |
| exposure | 0.2280 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
