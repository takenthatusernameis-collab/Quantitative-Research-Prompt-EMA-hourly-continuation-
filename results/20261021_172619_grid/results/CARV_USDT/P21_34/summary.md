# EMA Hourly Continuation — CARV/USDT P21_34

**Symbol:** CARV/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 337 |
| net_profit_factor | 0.6442 |
| net_win_rate | 0.4896 |
| gross_profit_factor | 0.9487 |
| gross_win_rate | 0.4896 |
| sharpe_ratio | -2.7554 |
| sortino_ratio | -0.8081 |
| max_drawdown | 0.5378 |
| cagr | -0.3079 |
| net_avg_win | 57.7025 |
| net_avg_loss | -85.9317 |
| avg_hold_time_bars | 7.0000 |
| exposure | 0.1328 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
