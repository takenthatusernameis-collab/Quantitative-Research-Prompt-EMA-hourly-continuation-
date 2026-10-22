# EMA Hourly Continuation — AERO/USDT P50_200

**Symbol:** AERO/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 371 |
| net_profit_factor | 0.6722 |
| net_win_rate | 0.4717 |
| gross_profit_factor | 0.9018 |
| gross_win_rate | 0.4744 |
| sharpe_ratio | -2.4282 |
| sortino_ratio | -0.6637 |
| max_drawdown | 0.5885 |
| cagr | -0.2674 |
| net_avg_win | 63.5303 |
| net_avg_loss | -84.3894 |
| avg_hold_time_bars | 22.2022 |
| exposure | 0.3744 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
