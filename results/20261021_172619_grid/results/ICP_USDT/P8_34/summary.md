# EMA Hourly Continuation — ICP/USDT P8_34

**Symbol:** ICP/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 695 |
| net_profit_factor | 0.8143 |
| net_win_rate | 0.5180 |
| gross_profit_factor | 1.0789 |
| gross_win_rate | 0.5180 |
| sharpe_ratio | -1.7566 |
| sortino_ratio | -0.6667 |
| max_drawdown | 0.5788 |
| cagr | -0.2652 |
| net_avg_win | 65.6401 |
| net_avg_loss | -86.6217 |
| avg_hold_time_bars | 8.1453 |
| exposure | 0.2573 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
