# EMA Hourly Continuation — REQ/USDT P21_55

**Symbol:** REQ/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 583 |
| net_profit_factor | 0.5786 |
| net_win_rate | 0.4511 |
| gross_profit_factor | 0.8930 |
| gross_win_rate | 0.4511 |
| sharpe_ratio | -4.9321 |
| sortino_ratio | -1.7055 |
| max_drawdown | 0.8647 |
| cagr | -0.5474 |
| net_avg_win | 45.0679 |
| net_avg_loss | -64.0222 |
| avg_hold_time_bars | 8.8645 |
| exposure | 0.2349 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
