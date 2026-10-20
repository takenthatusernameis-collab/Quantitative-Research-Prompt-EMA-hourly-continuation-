# EMA Hourly Continuation — ORCA/USDT P8_20

**Symbol:** ORCA/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1507 |
| net_profit_factor | 0.4979 |
| net_win_rate | 0.4565 |
| gross_profit_factor | 0.9517 |
| gross_win_rate | 0.4884 |
| sharpe_ratio | -9.1404 |
| sortino_ratio | -4.9898 |
| max_drawdown | 0.9982 |
| cagr | -0.9155 |
| net_avg_win | 14.3819 |
| net_avg_loss | -24.2668 |
| avg_hold_time_bars | 3.5786 |
| exposure | 0.2451 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
