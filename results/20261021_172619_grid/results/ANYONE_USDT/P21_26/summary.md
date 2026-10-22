# EMA Hourly Continuation — ANYONE/USDT P21_26

**Symbol:** ANYONE/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 210 |
| net_profit_factor | 0.7438 |
| net_win_rate | 0.4952 |
| gross_profit_factor | 0.9753 |
| gross_win_rate | 0.4952 |
| sharpe_ratio | -1.4574 |
| sortino_ratio | -0.3178 |
| max_drawdown | 0.3906 |
| cagr | -0.1369 |
| net_avg_win | 78.9833 |
| net_avg_loss | -104.1829 |
| avg_hold_time_bars | 5.2952 |
| exposure | 0.0562 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
