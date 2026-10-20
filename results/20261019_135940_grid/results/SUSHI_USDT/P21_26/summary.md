# EMA Hourly Continuation — SUSHI/USDT P21_26

**Symbol:** SUSHI/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1241 |
| net_profit_factor | 0.2414 |
| net_win_rate | 0.3537 |
| gross_profit_factor | 0.8330 |
| gross_win_rate | 0.4061 |
| sharpe_ratio | -14.9280 |
| sortino_ratio | -7.6421 |
| max_drawdown | 1.0000 |
| cagr | -0.9834 |
| net_avg_win | 7.2467 |
| net_avg_loss | -16.4351 |
| avg_hold_time_bars | 1.8268 |
| exposure | 0.1026 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
