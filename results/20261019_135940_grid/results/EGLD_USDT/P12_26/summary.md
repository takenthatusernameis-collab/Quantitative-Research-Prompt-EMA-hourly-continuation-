# EMA Hourly Continuation — EGLD/USDT P12_26

**Symbol:** EGLD/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1404 |
| net_profit_factor | 0.3658 |
| net_win_rate | 0.4202 |
| gross_profit_factor | 0.9386 |
| gross_win_rate | 0.4544 |
| sharpe_ratio | -11.4828 |
| sortino_ratio | -6.1020 |
| max_drawdown | 0.9996 |
| cagr | -0.9540 |
| net_avg_win | 9.7737 |
| net_avg_loss | -19.3637 |
| avg_hold_time_bars | 2.9423 |
| exposure | 0.1878 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
