# EMA Hourly Continuation — WIN/USDT P21_100

**Symbol:** WIN/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 410 |
| net_profit_factor | 0.7051 |
| net_win_rate | 0.4951 |
| gross_profit_factor | 0.9632 |
| gross_win_rate | 0.4951 |
| sharpe_ratio | -2.0989 |
| sortino_ratio | -0.6083 |
| max_drawdown | 0.5786 |
| cagr | -0.2446 |
| net_avg_win | 59.5569 |
| net_avg_loss | -82.8338 |
| avg_hold_time_bars | 21.3122 |
| exposure | 0.3972 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
