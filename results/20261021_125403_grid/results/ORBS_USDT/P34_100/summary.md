# EMA Hourly Continuation — ORBS/USDT P34_100

**Symbol:** ORBS/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 487 |
| net_profit_factor | 0.6627 |
| net_win_rate | 0.4702 |
| gross_profit_factor | 0.9374 |
| gross_win_rate | 0.4702 |
| sharpe_ratio | -3.2674 |
| sortino_ratio | -1.0281 |
| max_drawdown | 0.7054 |
| cagr | -0.3774 |
| net_avg_win | 59.6825 |
| net_avg_loss | -79.9412 |
| avg_hold_time_bars | 12.0082 |
| exposure | 0.2658 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
