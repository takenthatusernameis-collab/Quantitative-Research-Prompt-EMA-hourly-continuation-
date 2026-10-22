# EMA Hourly Continuation — SQD/USDT P55_144

**Symbol:** SQD/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 336 |
| net_profit_factor | 0.9103 |
| net_win_rate | 0.5208 |
| gross_profit_factor | 1.0853 |
| gross_win_rate | 0.5208 |
| sharpe_ratio | -0.5303 |
| sortino_ratio | -0.1423 |
| max_drawdown | 0.2431 |
| cagr | -0.0669 |
| net_avg_win | 89.7715 |
| net_avg_loss | -107.1955 |
| avg_hold_time_bars | 14.5685 |
| exposure | 0.2301 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
