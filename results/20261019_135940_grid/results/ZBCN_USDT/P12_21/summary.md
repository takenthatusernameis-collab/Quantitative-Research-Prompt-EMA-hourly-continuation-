# EMA Hourly Continuation — ZBCN/USDT P12_21

**Symbol:** ZBCN/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1590 |
| net_profit_factor | 0.3378 |
| net_win_rate | 0.4302 |
| gross_profit_factor | 0.6913 |
| gross_win_rate | 0.4396 |
| sharpe_ratio | -11.5083 |
| sortino_ratio | -6.5232 |
| max_drawdown | 0.9997 |
| cagr | -0.9642 |
| net_avg_win | 7.4550 |
| net_avg_loss | -16.6628 |
| avg_hold_time_bars | 2.1465 |
| exposure | 0.1579 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
