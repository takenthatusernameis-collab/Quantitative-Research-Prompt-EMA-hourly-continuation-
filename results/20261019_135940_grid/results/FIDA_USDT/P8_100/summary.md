# EMA Hourly Continuation — FIDA/USDT P8_100

**Symbol:** FIDA/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 703 |
| net_profit_factor | 0.5612 |
| net_win_rate | 0.4651 |
| gross_profit_factor | 0.8297 |
| gross_win_rate | 0.4694 |
| sharpe_ratio | -4.1528 |
| sortino_ratio | -1.5460 |
| max_drawdown | 0.8474 |
| cagr | -0.5204 |
| net_avg_win | 32.9818 |
| net_avg_loss | -51.1122 |
| avg_hold_time_bars | 20.5832 |
| exposure | 0.6548 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
