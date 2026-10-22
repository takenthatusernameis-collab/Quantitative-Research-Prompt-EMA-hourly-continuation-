# EMA Hourly Continuation — PENDLE/USDT P12_21

**Symbol:** PENDLE/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1475 |
| net_profit_factor | 0.4478 |
| net_win_rate | 0.4244 |
| gross_profit_factor | 0.9397 |
| gross_win_rate | 0.4475 |
| sharpe_ratio | -11.3250 |
| sortino_ratio | -6.1820 |
| max_drawdown | 0.9996 |
| cagr | -0.9535 |
| net_avg_win | 12.9465 |
| net_avg_loss | -21.3192 |
| avg_hold_time_bars | 2.3498 |
| exposure | 0.1575 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
