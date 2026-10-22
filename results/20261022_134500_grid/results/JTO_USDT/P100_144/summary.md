# EMA Hourly Continuation — JTO/USDT P100_144

**Symbol:** JTO/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 502 |
| net_profit_factor | 0.4579 |
| net_win_rate | 0.4323 |
| gross_profit_factor | 0.7537 |
| gross_win_rate | 0.4422 |
| sharpe_ratio | -5.0480 |
| sortino_ratio | -1.6039 |
| max_drawdown | 0.8525 |
| cagr | -0.5316 |
| net_avg_win | 33.1297 |
| net_avg_loss | -55.0878 |
| avg_hold_time_bars | 3.9920 |
| exposure | 0.0911 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
