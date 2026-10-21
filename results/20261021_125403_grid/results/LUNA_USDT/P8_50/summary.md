# EMA Hourly Continuation — LUNA/USDT P8_50

**Symbol:** LUNA/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 666 |
| net_profit_factor | 0.7402 |
| net_win_rate | 0.4715 |
| gross_profit_factor | 0.9460 |
| gross_win_rate | 0.4715 |
| sharpe_ratio | -3.0055 |
| sortino_ratio | -1.1057 |
| max_drawdown | 0.7343 |
| cagr | -0.3989 |
| net_avg_win | 65.4510 |
| net_avg_loss | -78.8813 |
| avg_hold_time_bars | 12.8904 |
| exposure | 0.3902 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
