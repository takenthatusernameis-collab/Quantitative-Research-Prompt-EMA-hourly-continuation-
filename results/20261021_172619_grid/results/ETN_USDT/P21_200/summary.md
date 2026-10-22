# EMA Hourly Continuation — ETN/USDT P21_200

**Symbol:** ETN/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 339 |
| net_profit_factor | 0.5404 |
| net_win_rate | 0.3953 |
| gross_profit_factor | 0.6491 |
| gross_win_rate | 0.3953 |
| sharpe_ratio | -3.8519 |
| sortino_ratio | -1.0895 |
| max_drawdown | 0.6575 |
| cagr | -0.3964 |
| net_avg_win | 57.3756 |
| net_avg_loss | -69.3979 |
| avg_hold_time_bars | 26.2006 |
| exposure | 0.4825 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
