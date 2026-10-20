# EMA Hourly Continuation — CATI/USDT P12_100

**Symbol:** CATI/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 598 |
| net_profit_factor | 0.5635 |
| net_win_rate | 0.4365 |
| gross_profit_factor | 0.8574 |
| gross_win_rate | 0.4582 |
| sharpe_ratio | -5.4875 |
| sortino_ratio | -2.0726 |
| max_drawdown | 0.8841 |
| cagr | -0.6316 |
| net_avg_win | 43.2841 |
| net_avg_loss | -59.4866 |
| avg_hold_time_bars | 17.8880 |
| exposure | 0.5864 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
