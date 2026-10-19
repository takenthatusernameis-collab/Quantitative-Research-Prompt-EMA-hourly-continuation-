# EMA Hourly Continuation — GRAM/USDT P21_26

**Symbol:** GRAM/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1205 |
| net_profit_factor | 0.1363 |
| net_win_rate | 0.3062 |
| gross_profit_factor | 0.5296 |
| gross_win_rate | 0.3768 |
| sharpe_ratio | -17.7391 |
| sortino_ratio | -9.3776 |
| max_drawdown | 1.0000 |
| cagr | -0.9948 |
| net_avg_win | 4.2749 |
| net_avg_loss | -13.8486 |
| avg_hold_time_bars | 1.7419 |
| exposure | 0.0954 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
