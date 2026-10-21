# EMA Hourly Continuation — CAKE/USDT P8_50

**Symbol:** CAKE/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 630 |
| net_profit_factor | 0.8048 |
| net_win_rate | 0.5127 |
| gross_profit_factor | 1.0646 |
| gross_win_rate | 0.5127 |
| sharpe_ratio | -1.8659 |
| sortino_ratio | -0.6727 |
| max_drawdown | 0.5631 |
| cagr | -0.2670 |
| net_avg_win | 69.1249 |
| net_avg_loss | -90.3716 |
| avg_hold_time_bars | 16.2746 |
| exposure | 0.4660 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
