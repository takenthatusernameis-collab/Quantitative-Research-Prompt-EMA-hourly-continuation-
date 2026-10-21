# EMA Hourly Continuation — ZRX/USDT P26_50

**Symbol:** ZRX/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 545 |
| net_profit_factor | 0.6137 |
| net_win_rate | 0.4606 |
| gross_profit_factor | 0.8868 |
| gross_win_rate | 0.4606 |
| sharpe_ratio | -3.9988 |
| sortino_ratio | -1.3357 |
| max_drawdown | 0.7911 |
| cagr | -0.4587 |
| net_avg_win | 49.7411 |
| net_avg_loss | -69.1990 |
| avg_hold_time_bars | 6.5266 |
| exposure | 0.1617 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
