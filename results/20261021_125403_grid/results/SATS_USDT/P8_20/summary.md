# EMA Hourly Continuation — SATS/USDT P8_20

**Symbol:** SATS/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 597 |
| net_profit_factor | 0.7169 |
| net_win_rate | 0.4941 |
| gross_profit_factor | 0.9645 |
| gross_win_rate | 0.4941 |
| sharpe_ratio | -2.5030 |
| sortino_ratio | -0.8727 |
| max_drawdown | 0.6759 |
| cagr | -0.3310 |
| net_avg_win | 54.6908 |
| net_avg_loss | -74.5222 |
| avg_hold_time_bars | 5.6600 |
| exposure | 0.1529 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
