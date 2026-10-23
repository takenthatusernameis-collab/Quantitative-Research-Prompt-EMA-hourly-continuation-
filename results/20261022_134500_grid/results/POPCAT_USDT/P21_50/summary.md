# EMA Hourly Continuation — POPCAT/USDT P21_50

**Symbol:** POPCAT/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 861 |
| net_profit_factor | 0.5385 |
| net_win_rate | 0.4286 |
| gross_profit_factor | 0.7908 |
| gross_win_rate | 0.4344 |
| sharpe_ratio | -7.0457 |
| sortino_ratio | -3.1294 |
| max_drawdown | 0.9631 |
| cagr | -0.7819 |
| net_avg_win | 30.4392 |
| net_avg_loss | -42.3976 |
| avg_hold_time_bars | 4.6829 |
| exposure | 0.2130 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
