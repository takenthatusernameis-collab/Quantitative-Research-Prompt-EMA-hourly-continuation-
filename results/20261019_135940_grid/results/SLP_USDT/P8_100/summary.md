# EMA Hourly Continuation — SLP/USDT P8_100

**Symbol:** SLP/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 730 |
| net_profit_factor | 0.6215 |
| net_win_rate | 0.4562 |
| gross_profit_factor | 0.9034 |
| gross_win_rate | 0.4658 |
| sharpe_ratio | -4.6607 |
| sortino_ratio | -1.7692 |
| max_drawdown | 0.8845 |
| cagr | -0.5718 |
| net_avg_win | 43.4494 |
| net_avg_loss | -58.6404 |
| avg_hold_time_bars | 20.1795 |
| exposure | 0.6696 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
