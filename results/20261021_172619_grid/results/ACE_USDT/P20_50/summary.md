# EMA Hourly Continuation — ACE/USDT P20_50

**Symbol:** ACE/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 533 |
| net_profit_factor | 0.7145 |
| net_win_rate | 0.5028 |
| gross_profit_factor | 0.9692 |
| gross_win_rate | 0.5028 |
| sharpe_ratio | -2.1321 |
| sortino_ratio | -0.7040 |
| max_drawdown | 0.5782 |
| cagr | -0.2753 |
| net_avg_win | 51.9275 |
| net_avg_loss | -73.5006 |
| avg_hold_time_bars | 8.4916 |
| exposure | 0.2048 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
