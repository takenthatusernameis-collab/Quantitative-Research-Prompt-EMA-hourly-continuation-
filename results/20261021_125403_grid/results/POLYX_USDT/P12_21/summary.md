# EMA Hourly Continuation — POLYX/USDT P12_21

**Symbol:** POLYX/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 502 |
| net_profit_factor | 0.6797 |
| net_win_rate | 0.5040 |
| gross_profit_factor | 1.0620 |
| gross_win_rate | 0.5040 |
| sharpe_ratio | -3.1517 |
| sortino_ratio | -1.0182 |
| max_drawdown | 0.7021 |
| cagr | -0.3709 |
| net_avg_win | 57.6972 |
| net_avg_loss | -86.2452 |
| avg_hold_time_bars | 4.8984 |
| exposure | 0.1118 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
