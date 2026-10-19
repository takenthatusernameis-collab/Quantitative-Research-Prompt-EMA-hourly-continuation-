# EMA Hourly Continuation — SAND/USDT P8_50

**Symbol:** SAND/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1022 |
| net_profit_factor | 0.5039 |
| net_win_rate | 0.4393 |
| gross_profit_factor | 0.8460 |
| gross_win_rate | 0.4481 |
| sharpe_ratio | -7.1095 |
| sortino_ratio | -3.1759 |
| max_drawdown | 0.9803 |
| cagr | -0.7907 |
| net_avg_win | 22.1758 |
| net_avg_loss | -34.4852 |
| avg_hold_time_bars | 10.0294 |
| exposure | 0.4659 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
