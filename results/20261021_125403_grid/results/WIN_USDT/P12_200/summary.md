# EMA Hourly Continuation — WIN/USDT P12_200

**Symbol:** WIN/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 287 |
| net_profit_factor | 0.8747 |
| net_win_rate | 0.5261 |
| gross_profit_factor | 1.0855 |
| gross_win_rate | 0.5261 |
| sharpe_ratio | -0.5845 |
| sortino_ratio | -0.1425 |
| max_drawdown | 0.3420 |
| cagr | -0.0664 |
| net_avg_win | 73.2583 |
| net_avg_loss | -92.9851 |
| avg_hold_time_bars | 56.6098 |
| exposure | 0.7385 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
