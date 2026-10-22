# EMA Hourly Continuation — ZRO/USDT P50_200

**Symbol:** ZRO/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 385 |
| net_profit_factor | 0.7250 |
| net_win_rate | 0.4883 |
| gross_profit_factor | 0.9738 |
| gross_win_rate | 0.4909 |
| sharpe_ratio | -2.0744 |
| sortino_ratio | -0.5966 |
| max_drawdown | 0.4946 |
| cagr | -0.2461 |
| net_avg_win | 67.6660 |
| net_avg_loss | -89.0725 |
| avg_hold_time_bars | 17.9662 |
| exposure | 0.3386 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
