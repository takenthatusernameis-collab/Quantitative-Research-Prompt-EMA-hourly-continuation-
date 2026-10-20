# EMA Hourly Continuation — LISTA/USDT P20_34

**Symbol:** LISTA/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 976 |
| net_profit_factor | 0.5296 |
| net_win_rate | 0.4406 |
| gross_profit_factor | 0.9576 |
| gross_win_rate | 0.4621 |
| sharpe_ratio | -7.8104 |
| sortino_ratio | -3.5901 |
| max_drawdown | 0.9831 |
| cagr | -0.8231 |
| net_avg_win | 25.7233 |
| net_avg_loss | -38.2522 |
| avg_hold_time_bars | 3.4385 |
| exposure | 0.1641 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
