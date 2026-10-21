# EMA Hourly Continuation — AERO/USDT P20_200

**Symbol:** AERO/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 253 |
| net_profit_factor | 0.9776 |
| net_win_rate | 0.5296 |
| gross_profit_factor | 1.1188 |
| gross_win_rate | 0.5296 |
| sharpe_ratio | -0.0742 |
| sortino_ratio | -0.0170 |
| max_drawdown | 0.2111 |
| cagr | -0.0124 |
| net_avg_win | 100.4095 |
| net_avg_loss | -115.6614 |
| avg_hold_time_bars | 57.0672 |
| exposure | 0.6563 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
