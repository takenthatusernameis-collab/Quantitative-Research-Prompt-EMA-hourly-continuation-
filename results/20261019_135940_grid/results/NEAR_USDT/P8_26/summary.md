# EMA Hourly Continuation — NEAR/USDT P8_26

**Symbol:** NEAR/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1589 |
| net_profit_factor | 0.4814 |
| net_win_rate | 0.4563 |
| gross_profit_factor | 0.8962 |
| gross_win_rate | 0.4644 |
| sharpe_ratio | -9.3254 |
| sortino_ratio | -5.2190 |
| max_drawdown | 0.9985 |
| cagr | -0.9243 |
| net_avg_win | 12.7845 |
| net_avg_loss | -22.2841 |
| avg_hold_time_bars | 3.5897 |
| exposure | 0.2593 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
