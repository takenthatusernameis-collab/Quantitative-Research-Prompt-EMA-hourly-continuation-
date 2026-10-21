# EMA Hourly Continuation — IOTA/USDT P12_50

**Symbol:** IOTA/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 685 |
| net_profit_factor | 0.7897 |
| net_win_rate | 0.5051 |
| gross_profit_factor | 1.0257 |
| gross_win_rate | 0.5051 |
| sharpe_ratio | -2.0387 |
| sortino_ratio | -0.7658 |
| max_drawdown | 0.6132 |
| cagr | -0.2969 |
| net_avg_win | 63.7288 |
| net_avg_loss | -82.3625 |
| avg_hold_time_bars | 10.1679 |
| exposure | 0.3166 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
