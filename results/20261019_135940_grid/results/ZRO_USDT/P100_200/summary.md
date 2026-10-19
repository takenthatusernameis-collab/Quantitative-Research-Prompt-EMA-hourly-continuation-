# EMA Hourly Continuation — ZRO/USDT P100_200

**Symbol:** ZRO/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 361 |
| net_profit_factor | 0.7662 |
| net_win_rate | 0.5235 |
| gross_profit_factor | 1.0995 |
| gross_win_rate | 0.5291 |
| sharpe_ratio | -1.5198 |
| sortino_ratio | -0.4256 |
| max_drawdown | 0.4451 |
| cagr | -0.1833 |
| net_avg_win | 65.2817 |
| net_avg_loss | -93.6216 |
| avg_hold_time_bars | 6.9972 |
| exposure | 0.1236 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
