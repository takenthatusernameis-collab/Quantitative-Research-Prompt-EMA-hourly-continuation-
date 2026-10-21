# EMA Hourly Continuation — KMNO/USDT P20_50

**Symbol:** KMNO/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 486 |
| net_profit_factor | 0.7387 |
| net_win_rate | 0.5021 |
| gross_profit_factor | 0.9972 |
| gross_win_rate | 0.5021 |
| sharpe_ratio | -2.0718 |
| sortino_ratio | -0.6583 |
| max_drawdown | 0.5424 |
| cagr | -0.2628 |
| net_avg_win | 61.3308 |
| net_avg_loss | -83.7140 |
| avg_hold_time_bars | 7.7366 |
| exposure | 0.1736 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
