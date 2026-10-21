# EMA Hourly Continuation — AIOZ/USDT P89_144

**Symbol:** AIOZ/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 275 |
| net_profit_factor | 0.8917 |
| net_win_rate | 0.5345 |
| gross_profit_factor | 1.1391 |
| gross_win_rate | 0.5345 |
| sharpe_ratio | -0.5678 |
| sortino_ratio | -0.1361 |
| max_drawdown | 0.2592 |
| cagr | -0.0630 |
| net_avg_win | 84.4032 |
| net_avg_loss | -108.7013 |
| avg_hold_time_bars | 6.9200 |
| exposure | 0.0865 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
