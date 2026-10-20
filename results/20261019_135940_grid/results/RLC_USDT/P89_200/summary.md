# EMA Hourly Continuation — RLC/USDT P89_200

**Symbol:** RLC/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 428 |
| net_profit_factor | 0.5478 |
| net_win_rate | 0.4533 |
| gross_profit_factor | 0.8211 |
| gross_win_rate | 0.4579 |
| sharpe_ratio | -3.6883 |
| sortino_ratio | -1.0750 |
| max_drawdown | 0.7304 |
| cagr | -0.4012 |
| net_avg_win | 45.2212 |
| net_avg_loss | -68.4389 |
| avg_hold_time_bars | 10.7944 |
| exposure | 0.2100 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
