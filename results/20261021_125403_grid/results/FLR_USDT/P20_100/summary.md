# EMA Hourly Continuation — FLR/USDT P20_100

**Symbol:** FLR/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 534 |
| net_profit_factor | 0.7134 |
| net_win_rate | 0.4850 |
| gross_profit_factor | 0.9371 |
| gross_win_rate | 0.4869 |
| sharpe_ratio | -2.4453 |
| sortino_ratio | -0.8072 |
| max_drawdown | 0.6307 |
| cagr | -0.3094 |
| net_avg_win | 58.1675 |
| net_avg_loss | -76.7924 |
| avg_hold_time_bars | 15.2210 |
| exposure | 0.3695 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
