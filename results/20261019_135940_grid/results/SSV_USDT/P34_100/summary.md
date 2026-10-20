# EMA Hourly Continuation — SSV/USDT P34_100

**Symbol:** SSV/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 678 |
| net_profit_factor | 0.5178 |
| net_win_rate | 0.4440 |
| gross_profit_factor | 0.8190 |
| gross_win_rate | 0.4572 |
| sharpe_ratio | -5.2376 |
| sortino_ratio | -1.9075 |
| max_drawdown | 0.9084 |
| cagr | -0.6038 |
| net_avg_win | 32.2286 |
| net_avg_loss | -49.6910 |
| avg_hold_time_bars | 9.9985 |
| exposure | 0.3068 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
