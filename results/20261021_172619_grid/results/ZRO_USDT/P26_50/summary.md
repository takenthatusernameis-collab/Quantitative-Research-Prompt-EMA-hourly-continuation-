# EMA Hourly Continuation — ZRO/USDT P26_50

**Symbol:** ZRO/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 383 |
| net_profit_factor | 0.7738 |
| net_win_rate | 0.4987 |
| gross_profit_factor | 0.9786 |
| gross_win_rate | 0.4987 |
| sharpe_ratio | -1.5400 |
| sortino_ratio | -0.4482 |
| max_drawdown | 0.4152 |
| cagr | -0.1866 |
| net_avg_win | 68.4474 |
| net_avg_loss | -87.9960 |
| avg_hold_time_bars | 6.5483 |
| exposure | 0.1228 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
