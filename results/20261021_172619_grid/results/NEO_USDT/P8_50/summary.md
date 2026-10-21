# EMA Hourly Continuation — NEO/USDT P8_50

**Symbol:** NEO/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 701 |
| net_profit_factor | 0.7000 |
| net_win_rate | 0.4793 |
| gross_profit_factor | 0.9241 |
| gross_win_rate | 0.4793 |
| sharpe_ratio | -3.1333 |
| sortino_ratio | -1.1843 |
| max_drawdown | 0.7542 |
| cagr | -0.4184 |
| net_avg_win | 51.6383 |
| net_avg_loss | -67.9083 |
| avg_hold_time_bars | 13.7190 |
| exposure | 0.4371 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
