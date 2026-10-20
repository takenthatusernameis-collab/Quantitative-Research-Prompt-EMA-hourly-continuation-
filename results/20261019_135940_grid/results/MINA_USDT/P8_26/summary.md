# EMA Hourly Continuation — MINA/USDT P8_26

**Symbol:** MINA/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1521 |
| net_profit_factor | 0.3712 |
| net_win_rate | 0.4464 |
| gross_profit_factor | 0.7596 |
| gross_win_rate | 0.4688 |
| sharpe_ratio | -9.6543 |
| sortino_ratio | -5.3047 |
| max_drawdown | 0.9986 |
| cagr | -0.9268 |
| net_avg_win | 8.6814 |
| net_avg_loss | -18.8605 |
| avg_hold_time_bars | 4.1913 |
| exposure | 0.2898 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
