# EMA Hourly Continuation — FLIP/USDT P21_89

**Symbol:** FLIP/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 382 |
| net_profit_factor | 0.6831 |
| net_win_rate | 0.4791 |
| gross_profit_factor | 0.9281 |
| gross_win_rate | 0.4817 |
| sharpe_ratio | -2.3696 |
| sortino_ratio | -0.6588 |
| max_drawdown | 0.5491 |
| cagr | -0.2615 |
| net_avg_win | 62.7650 |
| net_avg_loss | -84.4963 |
| avg_hold_time_bars | 23.8089 |
| exposure | 0.4134 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
