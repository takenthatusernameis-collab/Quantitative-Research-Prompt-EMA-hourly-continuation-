# EMA Hourly Continuation — EWT/USDT P100_200

**Symbol:** EWT/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 398 |
| net_profit_factor | 0.4613 |
| net_win_rate | 0.4221 |
| gross_profit_factor | 0.6937 |
| gross_win_rate | 0.4221 |
| sharpe_ratio | -4.4551 |
| sortino_ratio | -1.2463 |
| max_drawdown | 0.7900 |
| cagr | -0.4564 |
| net_avg_win | 39.9393 |
| net_avg_loss | -63.2439 |
| avg_hold_time_bars | 8.5528 |
| exposure | 0.1547 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
