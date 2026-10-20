# EMA Hourly Continuation — SUSHI/USDT P8_26

**Symbol:** SUSHI/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1532 |
| net_profit_factor | 0.4421 |
| net_win_rate | 0.4393 |
| gross_profit_factor | 0.8871 |
| gross_win_rate | 0.4589 |
| sharpe_ratio | -10.0295 |
| sortino_ratio | -5.5059 |
| max_drawdown | 0.9990 |
| cagr | -0.9355 |
| net_avg_win | 11.7632 |
| net_avg_loss | -20.8460 |
| avg_hold_time_bars | 4.0581 |
| exposure | 0.2813 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
