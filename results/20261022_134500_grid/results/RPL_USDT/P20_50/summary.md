# EMA Hourly Continuation — RPL/USDT P20_50

**Symbol:** RPL/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 906 |
| net_profit_factor | 0.5400 |
| net_win_rate | 0.4481 |
| gross_profit_factor | 0.9518 |
| gross_win_rate | 0.4614 |
| sharpe_ratio | -6.5502 |
| sortino_ratio | -2.7593 |
| max_drawdown | 0.9677 |
| cagr | -0.7409 |
| net_avg_win | 27.9554 |
| net_avg_loss | -42.0366 |
| avg_hold_time_bars | 6.3499 |
| exposure | 0.2604 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
