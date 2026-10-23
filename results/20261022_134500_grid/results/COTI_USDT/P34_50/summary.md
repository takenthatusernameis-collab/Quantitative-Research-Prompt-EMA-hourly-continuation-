# EMA Hourly Continuation — COTI/USDT P34_50

**Symbol:** COTI/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 956 |
| net_profit_factor | 0.4025 |
| net_win_rate | 0.4205 |
| gross_profit_factor | 0.8068 |
| gross_win_rate | 0.4331 |
| sharpe_ratio | -9.1699 |
| sortino_ratio | -4.0306 |
| max_drawdown | 0.9935 |
| cagr | -0.8649 |
| net_avg_win | 16.6486 |
| net_avg_loss | -30.0130 |
| avg_hold_time_bars | 2.5931 |
| exposure | 0.1127 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
