# EMA Hourly Continuation — ELON/USDT P8_20

**Symbol:** ELON/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1573 |
| net_profit_factor | 0.3280 |
| net_win_rate | 0.4209 |
| gross_profit_factor | 0.7267 |
| gross_win_rate | 0.4342 |
| sharpe_ratio | -12.1823 |
| sortino_ratio | -6.8974 |
| max_drawdown | 0.9998 |
| cagr | -0.9668 |
| net_avg_win | 7.3731 |
| net_avg_loss | -16.3326 |
| avg_hold_time_bars | 2.9536 |
| exposure | 0.2112 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
