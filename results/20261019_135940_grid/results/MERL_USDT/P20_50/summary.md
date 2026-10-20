# EMA Hourly Continuation — MERL/USDT P20_50

**Symbol:** MERL/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 964 |
| net_profit_factor | 0.6001 |
| net_win_rate | 0.4637 |
| gross_profit_factor | 0.8948 |
| gross_win_rate | 0.4699 |
| sharpe_ratio | -5.1819 |
| sortino_ratio | -2.2787 |
| max_drawdown | 0.9373 |
| cagr | -0.6592 |
| net_avg_win | 31.3103 |
| net_avg_loss | -45.1082 |
| avg_hold_time_bars | 5.5726 |
| exposure | 0.2449 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
