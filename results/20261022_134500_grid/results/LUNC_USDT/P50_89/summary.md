# EMA Hourly Continuation — LUNC/USDT P50_89

**Symbol:** LUNC/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 748 |
| net_profit_factor | 0.4124 |
| net_win_rate | 0.4612 |
| gross_profit_factor | 0.8475 |
| gross_win_rate | 0.4773 |
| sharpe_ratio | -6.9258 |
| sortino_ratio | -2.6738 |
| max_drawdown | 0.9669 |
| cagr | -0.7392 |
| net_avg_win | 19.6455 |
| net_avg_loss | -40.7832 |
| avg_hold_time_bars | 4.2553 |
| exposure | 0.1447 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
