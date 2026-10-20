# EMA Hourly Continuation — CSPR/USDT P20_34

**Symbol:** CSPR/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1387 |
| net_profit_factor | 0.2415 |
| net_win_rate | 0.3641 |
| gross_profit_factor | 0.6955 |
| gross_win_rate | 0.3886 |
| sharpe_ratio | -13.9446 |
| sortino_ratio | -7.4064 |
| max_drawdown | 0.9999 |
| cagr | -0.9787 |
| net_avg_win | 6.3038 |
| net_avg_loss | -14.9465 |
| avg_hold_time_bars | 2.5451 |
| exposure | 0.1605 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
