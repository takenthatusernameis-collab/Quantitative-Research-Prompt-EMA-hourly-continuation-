# EMA Hourly Continuation — TAIKO/USDT P20_26

**Symbol:** TAIKO/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 210 |
| net_profit_factor | 0.8251 |
| net_win_rate | 0.5571 |
| gross_profit_factor | 1.2405 |
| gross_win_rate | 0.5571 |
| sharpe_ratio | -0.8516 |
| sortino_ratio | -0.1842 |
| max_drawdown | 0.2804 |
| cagr | -0.0812 |
| net_avg_win | 73.5504 |
| net_avg_loss | -112.1425 |
| avg_hold_time_bars | 6.1571 |
| exposure | 0.0621 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
