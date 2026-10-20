# EMA Hourly Continuation — COTI/USDT P8_200

**Symbol:** COTI/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 431 |
| net_profit_factor | 0.8392 |
| net_win_rate | 0.5197 |
| gross_profit_factor | 1.1078 |
| gross_win_rate | 0.5244 |
| sharpe_ratio | -1.1766 |
| sortino_ratio | -0.3465 |
| max_drawdown | 0.4390 |
| cagr | -0.1527 |
| net_avg_win | 79.3055 |
| net_avg_loss | -102.2632 |
| avg_hold_time_bars | 40.1949 |
| exposure | 0.7875 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
