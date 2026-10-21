# EMA Hourly Continuation — KCS/USDT P100_200

**Symbol:** KCS/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 257 |
| net_profit_factor | 0.4676 |
| net_win_rate | 0.4553 |
| gross_profit_factor | 0.8319 |
| gross_win_rate | 0.4591 |
| sharpe_ratio | -3.4899 |
| sortino_ratio | -0.8025 |
| max_drawdown | 0.6108 |
| cagr | -0.3108 |
| net_avg_win | 45.5937 |
| net_avg_loss | -81.4841 |
| avg_hold_time_bars | 14.6459 |
| exposure | 0.1711 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
