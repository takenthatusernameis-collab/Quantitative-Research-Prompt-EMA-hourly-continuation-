# EMA Hourly Continuation — DEGEN/USDT P21_100

**Symbol:** DEGEN/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 462 |
| net_profit_factor | 0.9160 |
| net_win_rate | 0.5173 |
| gross_profit_factor | 1.0754 |
| gross_win_rate | 0.5173 |
| sharpe_ratio | -0.6457 |
| sortino_ratio | -0.1996 |
| max_drawdown | 0.3556 |
| cagr | -0.0926 |
| net_avg_win | 98.6062 |
| net_avg_loss | -115.3767 |
| avg_hold_time_bars | 19.4004 |
| exposure | 0.4081 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
