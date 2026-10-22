# EMA Hourly Continuation — ENA/USDT P21_144

**Symbol:** ENA/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 515 |
| net_profit_factor | 0.6794 |
| net_win_rate | 0.4660 |
| gross_profit_factor | 0.8621 |
| gross_win_rate | 0.4699 |
| sharpe_ratio | -2.6089 |
| sortino_ratio | -0.8381 |
| max_drawdown | 0.6383 |
| cagr | -0.3230 |
| net_avg_win | 55.1481 |
| net_avg_loss | -70.8418 |
| avg_hold_time_bars | 21.5146 |
| exposure | 0.5036 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
