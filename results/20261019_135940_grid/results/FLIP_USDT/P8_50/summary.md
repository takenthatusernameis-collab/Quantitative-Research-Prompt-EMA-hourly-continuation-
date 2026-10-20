# EMA Hourly Continuation — FLIP/USDT P8_50

**Symbol:** FLIP/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 719 |
| net_profit_factor | 0.5529 |
| net_win_rate | 0.4242 |
| gross_profit_factor | 0.9134 |
| gross_win_rate | 0.4520 |
| sharpe_ratio | -6.2521 |
| sortino_ratio | -2.3495 |
| max_drawdown | 0.9474 |
| cagr | -0.6851 |
| net_avg_win | 38.3216 |
| net_avg_loss | -51.0601 |
| avg_hold_time_bars | 16.2629 |
| exposure | 0.5315 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
