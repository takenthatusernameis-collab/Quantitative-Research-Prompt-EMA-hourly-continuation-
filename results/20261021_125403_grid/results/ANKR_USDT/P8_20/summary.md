# EMA Hourly Continuation — ANKR/USDT P8_20

**Symbol:** ANKR/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 694 |
| net_profit_factor | 0.6470 |
| net_win_rate | 0.4755 |
| gross_profit_factor | 0.9752 |
| gross_win_rate | 0.4755 |
| sharpe_ratio | -4.3872 |
| sortino_ratio | -1.6598 |
| max_drawdown | 0.8568 |
| cagr | -0.5316 |
| net_avg_win | 47.2727 |
| net_avg_loss | -66.2407 |
| avg_hold_time_bars | 5.4020 |
| exposure | 0.1704 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
