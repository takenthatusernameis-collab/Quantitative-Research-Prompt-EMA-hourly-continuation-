# EMA Hourly Continuation — NEAR/USDT P8_200

**Symbol:** NEAR/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 249 |
| net_profit_factor | 0.8649 |
| net_win_rate | 0.4980 |
| gross_profit_factor | 0.9856 |
| gross_win_rate | 0.4980 |
| sharpe_ratio | -0.6942 |
| sortino_ratio | -0.1566 |
| max_drawdown | 0.2695 |
| cagr | -0.0717 |
| net_avg_win | 87.9572 |
| net_avg_loss | -100.8792 |
| avg_hold_time_bars | 72.6426 |
| exposure | 0.8222 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
