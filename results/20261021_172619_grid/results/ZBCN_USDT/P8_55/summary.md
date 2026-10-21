# EMA Hourly Continuation — ZBCN/USDT P8_55

**Symbol:** ZBCN/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 714 |
| net_profit_factor | 0.9594 |
| net_win_rate | 0.5336 |
| gross_profit_factor | 1.1340 |
| gross_win_rate | 0.5336 |
| sharpe_ratio | -0.2858 |
| sortino_ratio | -0.1113 |
| max_drawdown | 0.3085 |
| cagr | -0.0612 |
| net_avg_win | 89.6191 |
| net_avg_loss | -106.8726 |
| avg_hold_time_bars | 11.6064 |
| exposure | 0.3834 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
