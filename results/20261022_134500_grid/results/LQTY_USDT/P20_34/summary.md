# EMA Hourly Continuation — LQTY/USDT P20_34

**Symbol:** LQTY/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1172 |
| net_profit_factor | 0.3958 |
| net_win_rate | 0.4488 |
| gross_profit_factor | 0.8241 |
| gross_win_rate | 0.4659 |
| sharpe_ratio | -9.0007 |
| sortino_ratio | -4.3734 |
| max_drawdown | 0.9956 |
| cagr | -0.8833 |
| net_avg_win | 12.3963 |
| net_avg_loss | -25.5049 |
| avg_hold_time_bars | 3.1758 |
| exposure | 0.1684 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
