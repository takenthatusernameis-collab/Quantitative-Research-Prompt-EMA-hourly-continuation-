# EMA Hourly Continuation — ZRO/USDT P89_144

**Symbol:** ZRO/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 437 |
| net_profit_factor | 0.4828 |
| net_win_rate | 0.4348 |
| gross_profit_factor | 0.7281 |
| gross_win_rate | 0.4371 |
| sharpe_ratio | -4.4689 |
| sortino_ratio | -1.3694 |
| max_drawdown | 0.7866 |
| cagr | -0.4801 |
| net_avg_win | 38.4476 |
| net_avg_loss | -61.2564 |
| avg_hold_time_bars | 4.3730 |
| exposure | 0.0935 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
