# EMA Hourly Continuation — ZKJ/USDT P26_100

**Symbol:** ZKJ/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 372 |
| net_profit_factor | 0.1611 |
| net_win_rate | 0.2769 |
| gross_profit_factor | 0.4501 |
| gross_win_rate | 0.3602 |
| sharpe_ratio | -9.6075 |
| sortino_ratio | -2.7916 |
| max_drawdown | 0.9790 |
| cagr | -0.7830 |
| net_avg_win | 18.2390 |
| net_avg_loss | -43.3567 |
| avg_hold_time_bars | 45.3898 |
| exposure | 0.7675 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
