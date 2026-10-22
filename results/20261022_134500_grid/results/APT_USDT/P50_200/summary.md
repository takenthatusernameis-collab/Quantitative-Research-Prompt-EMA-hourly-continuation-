# EMA Hourly Continuation — APT/USDT P50_200

**Symbol:** APT/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 385 |
| net_profit_factor | 0.6826 |
| net_win_rate | 0.4909 |
| gross_profit_factor | 0.9957 |
| gross_win_rate | 0.4987 |
| sharpe_ratio | -2.3024 |
| sortino_ratio | -0.6357 |
| max_drawdown | 0.5534 |
| cagr | -0.2620 |
| net_avg_win | 60.7418 |
| net_avg_loss | -85.8047 |
| avg_hold_time_bars | 22.4468 |
| exposure | 0.3928 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
