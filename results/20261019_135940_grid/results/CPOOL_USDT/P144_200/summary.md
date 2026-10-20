# EMA Hourly Continuation — CPOOL/USDT P144_200

**Symbol:** CPOOL/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 471 |
| net_profit_factor | 0.5040 |
| net_win_rate | 0.4374 |
| gross_profit_factor | 0.7906 |
| gross_win_rate | 0.4416 |
| sharpe_ratio | -4.8066 |
| sortino_ratio | -1.4680 |
| max_drawdown | 0.8500 |
| cagr | -0.5114 |
| net_avg_win | 41.1675 |
| net_avg_loss | -63.4923 |
| avg_hold_time_bars | 4.3100 |
| exposure | 0.0923 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
