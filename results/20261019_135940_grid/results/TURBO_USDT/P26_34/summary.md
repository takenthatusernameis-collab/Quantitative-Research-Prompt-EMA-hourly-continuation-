# EMA Hourly Continuation — TURBO/USDT P26_34

**Symbol:** TURBO/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 919 |
| net_profit_factor | 0.3868 |
| net_win_rate | 0.4059 |
| gross_profit_factor | 0.7410 |
| gross_win_rate | 0.4320 |
| sharpe_ratio | -10.9877 |
| sortino_ratio | -5.1720 |
| max_drawdown | 0.9963 |
| cagr | -0.9306 |
| net_avg_win | 16.8508 |
| net_avg_loss | -29.7577 |
| avg_hold_time_bars | 2.1099 |
| exposure | 0.1058 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
