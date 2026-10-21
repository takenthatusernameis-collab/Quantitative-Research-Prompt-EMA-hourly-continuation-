# EMA Hourly Continuation — ATH/USDT P21_144

**Symbol:** ATH/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 370 |
| net_profit_factor | 0.9753 |
| net_win_rate | 0.5405 |
| gross_profit_factor | 1.1607 |
| gross_win_rate | 0.5405 |
| sharpe_ratio | -0.0973 |
| sortino_ratio | -0.0279 |
| max_drawdown | 0.1281 |
| cagr | -0.0198 |
| net_avg_win | 90.9020 |
| net_avg_loss | -109.6525 |
| avg_hold_time_bars | 27.6757 |
| exposure | 0.4963 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
