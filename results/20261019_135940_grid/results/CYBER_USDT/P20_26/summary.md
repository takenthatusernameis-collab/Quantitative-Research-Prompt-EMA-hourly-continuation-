# EMA Hourly Continuation — CYBER/USDT P20_26

**Symbol:** CYBER/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1198 |
| net_profit_factor | 0.2562 |
| net_win_rate | 0.3715 |
| gross_profit_factor | 0.6859 |
| gross_win_rate | 0.4199 |
| sharpe_ratio | -13.4239 |
| sortino_ratio | -6.7251 |
| max_drawdown | 0.9998 |
| cagr | -0.9686 |
| net_avg_win | 7.7394 |
| net_avg_loss | -17.8518 |
| avg_hold_time_bars | 2.6903 |
| exposure | 0.1465 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
