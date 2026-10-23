# EMA Hourly Continuation — SATS/USDT P55_200

**Symbol:** SATS/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 375 |
| net_profit_factor | 0.5233 |
| net_win_rate | 0.4320 |
| gross_profit_factor | 0.7432 |
| gross_win_rate | 0.4373 |
| sharpe_ratio | -3.4900 |
| sortino_ratio | -0.9450 |
| max_drawdown | 0.6864 |
| cagr | -0.3632 |
| net_avg_win | 46.0508 |
| net_avg_loss | -66.9356 |
| avg_hold_time_bars | 20.7760 |
| exposure | 0.3525 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
