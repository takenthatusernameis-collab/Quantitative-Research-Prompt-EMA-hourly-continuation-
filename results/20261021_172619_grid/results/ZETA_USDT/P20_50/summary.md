# EMA Hourly Continuation — ZETA/USDT P20_50

**Symbol:** ZETA/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 549 |
| net_profit_factor | 0.7046 |
| net_win_rate | 0.4827 |
| gross_profit_factor | 0.9374 |
| gross_win_rate | 0.4827 |
| sharpe_ratio | -2.7020 |
| sortino_ratio | -0.9035 |
| max_drawdown | 0.6512 |
| cagr | -0.3377 |
| net_avg_win | 58.1655 |
| net_avg_loss | -77.0310 |
| avg_hold_time_bars | 8.3625 |
| exposure | 0.2077 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
