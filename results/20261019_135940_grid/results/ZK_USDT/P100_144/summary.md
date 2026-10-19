# EMA Hourly Continuation — ZK/USDT P100_144

**Symbol:** ZK/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 481 |
| net_profit_factor | 0.5075 |
| net_win_rate | 0.4470 |
| gross_profit_factor | 0.8585 |
| gross_win_rate | 0.4595 |
| sharpe_ratio | -4.8668 |
| sortino_ratio | -1.5591 |
| max_drawdown | 0.8394 |
| cagr | -0.5303 |
| net_avg_win | 39.7532 |
| net_avg_loss | -63.3182 |
| avg_hold_time_bars | 5.2204 |
| exposure | 0.1224 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
