# EMA Hourly Continuation — CHZ/USDT P50_144

**Symbol:** CHZ/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 339 |
| net_profit_factor | 0.7518 |
| net_win_rate | 0.4926 |
| gross_profit_factor | 0.9654 |
| gross_win_rate | 0.4956 |
| sharpe_ratio | -1.5878 |
| sortino_ratio | -0.4178 |
| max_drawdown | 0.4132 |
| cagr | -0.1759 |
| net_avg_win | 69.7838 |
| net_avg_loss | -90.1234 |
| avg_hold_time_bars | 18.1563 |
| exposure | 0.2798 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
