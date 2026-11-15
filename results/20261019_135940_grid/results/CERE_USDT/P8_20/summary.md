# EMA Hourly Continuation — CERE/USDT P8_20

**Symbol:** CERE/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1611 |
| net_profit_factor | 0.2630 |
| net_win_rate | 0.2582 |
| gross_profit_factor | 0.6792 |
| gross_win_rate | 0.3389 |
| sharpe_ratio | -20.4157 |
| sortino_ratio | -12.0436 |
| max_drawdown | 1.0000 |
| cagr | -0.9987 |
| net_avg_win | 8.5799 |
| net_avg_loss | -11.3550 |
| avg_hold_time_bars | 3.6654 |
| exposure | 0.2684 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
