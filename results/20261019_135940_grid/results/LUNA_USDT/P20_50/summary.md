# EMA Hourly Continuation — LUNA/USDT P20_50

**Symbol:** LUNA/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1109 |
| net_profit_factor | 0.4677 |
| net_win_rate | 0.4211 |
| gross_profit_factor | 0.9024 |
| gross_win_rate | 0.4409 |
| sharpe_ratio | -9.5756 |
| sortino_ratio | -4.5214 |
| max_drawdown | 0.9965 |
| cagr | -0.8944 |
| net_avg_win | 18.7509 |
| net_avg_loss | -29.1610 |
| avg_hold_time_bars | 3.9639 |
| exposure | 0.1998 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
