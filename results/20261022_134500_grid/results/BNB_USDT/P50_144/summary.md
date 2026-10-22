# EMA Hourly Continuation — BNB/USDT P50_144

**Symbol:** BNB/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 564 |
| net_profit_factor | 0.3808 |
| net_win_rate | 0.4592 |
| gross_profit_factor | 0.9440 |
| gross_win_rate | 0.4911 |
| sharpe_ratio | -6.3876 |
| sortino_ratio | -2.1341 |
| max_drawdown | 0.9374 |
| cagr | -0.6632 |
| net_avg_win | 22.1964 |
| net_avg_loss | -49.5040 |
| avg_hold_time_bars | 9.7394 |
| exposure | 0.2497 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
