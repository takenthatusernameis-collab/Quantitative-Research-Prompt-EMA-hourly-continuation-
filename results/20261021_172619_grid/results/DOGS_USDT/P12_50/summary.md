# EMA Hourly Continuation — DOGS/USDT P12_50

**Symbol:** DOGS/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 503 |
| net_profit_factor | 0.7208 |
| net_win_rate | 0.4751 |
| gross_profit_factor | 0.8827 |
| gross_win_rate | 0.4751 |
| sharpe_ratio | -2.3556 |
| sortino_ratio | -0.8131 |
| max_drawdown | 0.5675 |
| cagr | -0.3121 |
| net_avg_win | 59.7247 |
| net_avg_loss | -75.0100 |
| avg_hold_time_bars | 11.3459 |
| exposure | 0.3028 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
