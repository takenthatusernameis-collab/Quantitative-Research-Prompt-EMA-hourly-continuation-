# EMA Hourly Continuation — POLYX/USDT P8_12

**Symbol:** POLYX/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 440 |
| net_profit_factor | 0.6238 |
| net_win_rate | 0.4818 |
| gross_profit_factor | 0.9901 |
| gross_win_rate | 0.4841 |
| sharpe_ratio | -3.5482 |
| sortino_ratio | -1.0709 |
| max_drawdown | 0.7085 |
| cagr | -0.3862 |
| net_avg_win | 55.2559 |
| net_avg_loss | -82.3615 |
| avg_hold_time_bars | 4.9091 |
| exposure | 0.0982 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
