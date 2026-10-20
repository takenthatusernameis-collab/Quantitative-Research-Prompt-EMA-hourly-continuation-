# EMA Hourly Continuation — POLYX/USDT P34_55

**Symbol:** POLYX/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 852 |
| net_profit_factor | 0.5225 |
| net_win_rate | 0.4589 |
| gross_profit_factor | 0.9918 |
| gross_win_rate | 0.4906 |
| sharpe_ratio | -6.8006 |
| sortino_ratio | -2.8030 |
| max_drawdown | 0.9702 |
| cagr | -0.7479 |
| net_avg_win | 27.1024 |
| net_avg_loss | -43.9974 |
| avg_hold_time_bars | 3.7195 |
| exposure | 0.1440 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
