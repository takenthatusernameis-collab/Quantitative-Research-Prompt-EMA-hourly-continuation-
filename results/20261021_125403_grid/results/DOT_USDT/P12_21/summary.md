# EMA Hourly Continuation — DOT/USDT P12_21

**Symbol:** DOT/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 268 |
| net_profit_factor | 0.6633 |
| net_win_rate | 0.4813 |
| gross_profit_factor | 0.9572 |
| gross_win_rate | 0.4813 |
| sharpe_ratio | -2.2288 |
| sortino_ratio | -0.5235 |
| max_drawdown | 0.4920 |
| cagr | -0.2119 |
| net_avg_win | 68.7252 |
| net_avg_loss | -96.1635 |
| avg_hold_time_bars | 4.9627 |
| exposure | 0.0605 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
