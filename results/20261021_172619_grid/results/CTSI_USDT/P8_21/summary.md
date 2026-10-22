# EMA Hourly Continuation — CTSI/USDT P8_21

**Symbol:** CTSI/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 755 |
| net_profit_factor | 0.7270 |
| net_win_rate | 0.4954 |
| gross_profit_factor | 1.0491 |
| gross_win_rate | 0.4954 |
| sharpe_ratio | -3.3850 |
| sortino_ratio | -1.3355 |
| max_drawdown | 0.7831 |
| cagr | -0.4558 |
| net_avg_win | 55.7482 |
| net_avg_loss | -75.2765 |
| avg_hold_time_bars | 5.8411 |
| exposure | 0.2005 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
