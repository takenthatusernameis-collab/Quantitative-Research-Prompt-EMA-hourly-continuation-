# EMA Hourly Continuation — OGN/USDT P89_144

**Symbol:** OGN/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 534 |
| net_profit_factor | 0.3809 |
| net_win_rate | 0.4157 |
| gross_profit_factor | 0.6936 |
| gross_win_rate | 0.4288 |
| sharpe_ratio | -6.2337 |
| sortino_ratio | -2.0338 |
| max_drawdown | 0.9226 |
| cagr | -0.6313 |
| net_avg_win | 25.4809 |
| net_avg_loss | -47.5946 |
| avg_hold_time_bars | 5.4569 |
| exposure | 0.1319 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
