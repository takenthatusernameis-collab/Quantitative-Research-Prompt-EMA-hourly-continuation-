# EMA Hourly Continuation — SQD/USDT P12_21

**Symbol:** SQD/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 339 |
| net_profit_factor | 0.7366 |
| net_win_rate | 0.4808 |
| gross_profit_factor | 0.9507 |
| gross_win_rate | 0.4808 |
| sharpe_ratio | -1.9533 |
| sortino_ratio | -0.5220 |
| max_drawdown | 0.5209 |
| cagr | -0.2126 |
| net_avg_win | 75.5434 |
| net_avg_loss | -94.9877 |
| avg_hold_time_bars | 4.9351 |
| exposure | 0.0786 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
