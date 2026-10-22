# EMA Hourly Continuation — ICP/USDT P8_89

**Symbol:** ICP/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 693 |
| net_profit_factor | 0.6246 |
| net_win_rate | 0.4834 |
| gross_profit_factor | 0.9343 |
| gross_win_rate | 0.4834 |
| sharpe_ratio | -3.9549 |
| sortino_ratio | -1.4560 |
| max_drawdown | 0.8411 |
| cagr | -0.5090 |
| net_avg_win | 41.3481 |
| net_avg_loss | -61.9447 |
| avg_hold_time_bars | 21.1284 |
| exposure | 0.6655 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
