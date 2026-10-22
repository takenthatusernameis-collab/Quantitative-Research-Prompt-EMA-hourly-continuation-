# EMA Hourly Continuation — IOTX/USDT P50_100

**Symbol:** IOTX/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 385 |
| net_profit_factor | 0.6910 |
| net_win_rate | 0.4883 |
| gross_profit_factor | 0.9357 |
| gross_win_rate | 0.4883 |
| sharpe_ratio | -2.1796 |
| sortino_ratio | -0.6126 |
| max_drawdown | 0.5096 |
| cagr | -0.2442 |
| net_avg_win | 60.0755 |
| net_avg_loss | -82.9641 |
| avg_hold_time_bars | 8.6234 |
| exposure | 0.1509 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
