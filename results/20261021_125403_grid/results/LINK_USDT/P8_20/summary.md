# EMA Hourly Continuation — LINK/USDT P8_20

**Symbol:** LINK/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 455 |
| net_profit_factor | 0.7742 |
| net_win_rate | 0.5253 |
| gross_profit_factor | 1.0931 |
| gross_win_rate | 0.5253 |
| sharpe_ratio | -1.6709 |
| sortino_ratio | -0.5146 |
| max_drawdown | 0.5176 |
| cagr | -0.2096 |
| net_avg_win | 64.0197 |
| net_avg_loss | -91.4916 |
| avg_hold_time_bars | 6.0462 |
| exposure | 0.1250 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
