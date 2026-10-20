# EMA Hourly Continuation — FLIP/USDT P89_144

**Symbol:** FLIP/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 305 |
| net_profit_factor | 0.4069 |
| net_win_rate | 0.4131 |
| gross_profit_factor | 0.7928 |
| gross_win_rate | 0.4361 |
| sharpe_ratio | -4.9716 |
| sortino_ratio | -1.2160 |
| max_drawdown | 0.7893 |
| cagr | -0.4596 |
| net_avg_win | 42.8334 |
| net_avg_loss | -74.1052 |
| avg_hold_time_bars | 11.3180 |
| exposure | 0.1569 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
