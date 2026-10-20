# EMA Hourly Continuation — TURBO/USDT P21_100

**Symbol:** TURBO/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 576 |
| net_profit_factor | 0.6527 |
| net_win_rate | 0.4549 |
| gross_profit_factor | 0.9009 |
| gross_win_rate | 0.4635 |
| sharpe_ratio | -4.1457 |
| sortino_ratio | -1.5349 |
| max_drawdown | 0.7945 |
| cagr | -0.5173 |
| net_avg_win | 56.0969 |
| net_avg_loss | -71.7172 |
| avg_hold_time_bars | 13.0208 |
| exposure | 0.4092 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
