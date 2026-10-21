# EMA Hourly Continuation — RLC/USDT P50_200

**Symbol:** RLC/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 318 |
| net_profit_factor | 0.7383 |
| net_win_rate | 0.4811 |
| gross_profit_factor | 0.9089 |
| gross_win_rate | 0.4811 |
| sharpe_ratio | -1.6189 |
| sortino_ratio | -0.4115 |
| max_drawdown | 0.3962 |
| cagr | -0.1729 |
| net_avg_win | 69.8894 |
| net_avg_loss | -87.7823 |
| avg_hold_time_bars | 28.9780 |
| exposure | 0.4189 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
