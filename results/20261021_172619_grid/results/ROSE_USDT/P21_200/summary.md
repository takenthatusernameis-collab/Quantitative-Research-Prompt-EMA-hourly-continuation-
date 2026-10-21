# EMA Hourly Continuation — ROSE/USDT P21_200

**Symbol:** ROSE/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 284 |
| net_profit_factor | 0.8506 |
| net_win_rate | 0.5035 |
| gross_profit_factor | 0.9957 |
| gross_win_rate | 0.5035 |
| sharpe_ratio | -0.7995 |
| sortino_ratio | -0.1926 |
| max_drawdown | 0.2649 |
| cagr | -0.0870 |
| net_avg_win | 81.2979 |
| net_avg_loss | -96.9357 |
| avg_hold_time_bars | 52.0915 |
| exposure | 0.6725 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
