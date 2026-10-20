# EMA Hourly Continuation — SYN/USDT P8_34

**Symbol:** SYN/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1315 |
| net_profit_factor | 0.5649 |
| net_win_rate | 0.4631 |
| gross_profit_factor | 0.9101 |
| gross_win_rate | 0.4722 |
| sharpe_ratio | -6.8652 |
| sortino_ratio | -3.4866 |
| max_drawdown | 0.9861 |
| cagr | -0.8178 |
| net_avg_win | 21.0198 |
| net_avg_loss | -32.0993 |
| avg_hold_time_bars | 5.8707 |
| exposure | 0.3509 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
