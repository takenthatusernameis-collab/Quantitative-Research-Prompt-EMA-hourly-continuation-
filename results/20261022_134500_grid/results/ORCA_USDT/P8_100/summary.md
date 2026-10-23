# EMA Hourly Continuation — ORCA/USDT P8_100

**Symbol:** ORCA/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 624 |
| net_profit_factor | 0.6918 |
| net_win_rate | 0.4872 |
| gross_profit_factor | 0.9825 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -2.9641 |
| sortino_ratio | -1.0397 |
| max_drawdown | 0.7374 |
| cagr | -0.3926 |
| net_avg_win | 52.7313 |
| net_avg_loss | -72.4086 |
| avg_hold_time_bars | 23.6474 |
| exposure | 0.6707 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
