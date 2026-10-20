# EMA Hourly Continuation — ENJ/USDT P100_200

**Symbol:** ENJ/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 336 |
| net_profit_factor | 0.6608 |
| net_win_rate | 0.5030 |
| gross_profit_factor | 1.0318 |
| gross_win_rate | 0.5119 |
| sharpe_ratio | -2.2950 |
| sortino_ratio | -0.5930 |
| max_drawdown | 0.5239 |
| cagr | -0.2477 |
| net_avg_win | 58.8718 |
| net_avg_loss | -90.1554 |
| avg_hold_time_bars | 13.1756 |
| exposure | 0.2012 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
