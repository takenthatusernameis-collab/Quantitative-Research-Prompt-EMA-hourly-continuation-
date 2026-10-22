# EMA Hourly Continuation — ETHFI/USDT P26_144

**Symbol:** ETHFI/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 549 |
| net_profit_factor | 0.7475 |
| net_win_rate | 0.4900 |
| gross_profit_factor | 0.9891 |
| gross_win_rate | 0.4900 |
| sharpe_ratio | -2.3822 |
| sortino_ratio | -0.7917 |
| max_drawdown | 0.6167 |
| cagr | -0.3100 |
| net_avg_win | 66.6957 |
| net_avg_loss | -85.7254 |
| avg_hold_time_bars | 18.8525 |
| exposure | 0.4705 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
