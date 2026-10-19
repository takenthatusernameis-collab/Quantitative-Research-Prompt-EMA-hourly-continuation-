# EMA Hourly Continuation — SAND/USDT P89_100

**Symbol:** SAND/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 561 |
| net_profit_factor | 0.2616 |
| net_win_rate | 0.3815 |
| gross_profit_factor | 0.8404 |
| gross_win_rate | 0.4456 |
| sharpe_ratio | -9.1148 |
| sortino_ratio | -3.1400 |
| max_drawdown | 0.9843 |
| cagr | -0.8087 |
| net_avg_win | 16.2967 |
| net_avg_loss | -38.4163 |
| avg_hold_time_bars | 1.7914 |
| exposure | 0.0457 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
