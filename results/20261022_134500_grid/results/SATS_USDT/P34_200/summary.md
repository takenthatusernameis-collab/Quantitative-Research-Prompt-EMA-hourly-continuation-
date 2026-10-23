# EMA Hourly Continuation — SATS/USDT P34_200

**Symbol:** SATS/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 393 |
| net_profit_factor | 0.5337 |
| net_win_rate | 0.4275 |
| gross_profit_factor | 0.7697 |
| gross_win_rate | 0.4351 |
| sharpe_ratio | -3.6106 |
| sortino_ratio | -0.9997 |
| max_drawdown | 0.7035 |
| cagr | -0.3789 |
| net_avg_win | 47.6418 |
| net_avg_loss | -66.6473 |
| avg_hold_time_bars | 25.7023 |
| exposure | 0.4571 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
