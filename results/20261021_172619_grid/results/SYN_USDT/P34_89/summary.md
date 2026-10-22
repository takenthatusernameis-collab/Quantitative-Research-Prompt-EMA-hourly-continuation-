# EMA Hourly Continuation — SYN/USDT P34_89

**Symbol:** SYN/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 437 |
| net_profit_factor | 0.8627 |
| net_win_rate | 0.5172 |
| gross_profit_factor | 1.0763 |
| gross_win_rate | 0.5172 |
| sharpe_ratio | -1.0114 |
| sortino_ratio | -0.3040 |
| max_drawdown | 0.3623 |
| cagr | -0.1330 |
| net_avg_win | 83.7560 |
| net_avg_loss | -103.9895 |
| avg_hold_time_bars | 13.0023 |
| exposure | 0.2583 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
