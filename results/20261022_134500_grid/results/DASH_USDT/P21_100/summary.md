# EMA Hourly Continuation — DASH/USDT P21_100

**Symbol:** DASH/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 668 |
| net_profit_factor | 0.5306 |
| net_win_rate | 0.4446 |
| gross_profit_factor | 0.8845 |
| gross_win_rate | 0.4506 |
| sharpe_ratio | -5.3890 |
| sortino_ratio | -1.9666 |
| max_drawdown | 0.9099 |
| cagr | -0.6093 |
| net_avg_win | 34.4720 |
| net_avg_loss | -52.0062 |
| avg_hold_time_bars | 13.6976 |
| exposure | 0.4159 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
