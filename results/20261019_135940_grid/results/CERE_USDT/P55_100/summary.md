# EMA Hourly Continuation — CERE/USDT P55_100

**Symbol:** CERE/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 703 |
| net_profit_factor | 0.4289 |
| net_win_rate | 0.3243 |
| gross_profit_factor | 0.8222 |
| gross_win_rate | 0.3528 |
| sharpe_ratio | -10.8612 |
| sortino_ratio | -4.1535 |
| max_drawdown | 0.9959 |
| cagr | -0.8880 |
| net_avg_win | 32.8100 |
| net_avg_loss | -36.7152 |
| avg_hold_time_bars | 5.9886 |
| exposure | 0.1914 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
