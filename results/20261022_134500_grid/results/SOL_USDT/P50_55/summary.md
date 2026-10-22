# EMA Hourly Continuation — SOL/USDT P50_55

**Symbol:** SOL/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 760 |
| net_profit_factor | 0.1085 |
| net_win_rate | 0.3289 |
| gross_profit_factor | 0.4337 |
| gross_win_rate | 0.3974 |
| sharpe_ratio | -13.4396 |
| sortino_ratio | -5.6225 |
| max_drawdown | 0.9997 |
| cagr | -0.9596 |
| net_avg_win | 4.8644 |
| net_avg_loss | -21.9862 |
| avg_hold_time_bars | 1.8750 |
| exposure | 0.0648 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
