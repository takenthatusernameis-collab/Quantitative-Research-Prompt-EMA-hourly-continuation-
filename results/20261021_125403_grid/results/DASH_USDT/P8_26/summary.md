# EMA Hourly Continuation — DASH/USDT P8_26

**Symbol:** DASH/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 615 |
| net_profit_factor | 0.7854 |
| net_win_rate | 0.5252 |
| gross_profit_factor | 1.0866 |
| gross_win_rate | 0.5252 |
| sharpe_ratio | -1.6609 |
| sortino_ratio | -0.5940 |
| max_drawdown | 0.5189 |
| cagr | -0.2396 |
| net_avg_win | 56.3562 |
| net_avg_loss | -79.3738 |
| avg_hold_time_bars | 6.8813 |
| exposure | 0.1924 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
