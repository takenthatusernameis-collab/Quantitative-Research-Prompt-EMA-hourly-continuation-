# EMA Hourly Continuation — LQTY/USDT P8_100

**Symbol:** LQTY/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 386 |
| net_profit_factor | 0.8719 |
| net_win_rate | 0.5130 |
| gross_profit_factor | 1.0426 |
| gross_win_rate | 0.5130 |
| sharpe_ratio | -0.8134 |
| sortino_ratio | -0.2287 |
| max_drawdown | 0.2876 |
| cagr | -0.1030 |
| net_avg_win | 82.4239 |
| net_avg_loss | -99.5592 |
| avg_hold_time_bars | 42.3497 |
| exposure | 0.7397 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
