# EMA Hourly Continuation — OP/USDT P20_144

**Symbol:** OP/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 339 |
| net_profit_factor | 0.7318 |
| net_win_rate | 0.4661 |
| gross_profit_factor | 0.8805 |
| gross_win_rate | 0.4661 |
| sharpe_ratio | -1.8941 |
| sortino_ratio | -0.4948 |
| max_drawdown | 0.4682 |
| cagr | -0.2039 |
| net_avg_win | 75.2817 |
| net_avg_loss | -89.8034 |
| avg_hold_time_bars | 36.1475 |
| exposure | 0.5570 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
