# EMA Hourly Continuation — FLIP/USDT P21_200

**Symbol:** FLIP/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 302 |
| net_profit_factor | 0.6501 |
| net_win_rate | 0.4669 |
| gross_profit_factor | 0.8609 |
| gross_win_rate | 0.4702 |
| sharpe_ratio | -2.2056 |
| sortino_ratio | -0.5400 |
| max_drawdown | 0.4971 |
| cagr | -0.2245 |
| net_avg_win | 62.1734 |
| net_avg_loss | -83.7565 |
| avg_hold_time_bars | 44.7417 |
| exposure | 0.6142 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
