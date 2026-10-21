# EMA Hourly Continuation — IOTA/USDT P8_21

**Symbol:** IOTA/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 672 |
| net_profit_factor | 0.7295 |
| net_win_rate | 0.5104 |
| gross_profit_factor | 1.0394 |
| gross_win_rate | 0.5104 |
| sharpe_ratio | -2.6188 |
| sortino_ratio | -0.9776 |
| max_drawdown | 0.6917 |
| cagr | -0.3596 |
| net_avg_win | 52.9547 |
| net_avg_loss | -75.6796 |
| avg_hold_time_bars | 5.2857 |
| exposure | 0.1615 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
