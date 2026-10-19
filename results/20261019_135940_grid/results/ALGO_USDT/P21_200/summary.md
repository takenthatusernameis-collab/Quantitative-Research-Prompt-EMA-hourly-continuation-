# EMA Hourly Continuation — ALGO/USDT P21_200

**Symbol:** ALGO/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 367 |
| net_profit_factor | 0.7259 |
| net_win_rate | 0.4959 |
| gross_profit_factor | 0.9822 |
| gross_win_rate | 0.4986 |
| sharpe_ratio | -1.9025 |
| sortino_ratio | -0.5122 |
| max_drawdown | 0.4714 |
| cagr | -0.2175 |
| net_avg_win | 66.9072 |
| net_avg_loss | -90.6817 |
| avg_hold_time_bars | 36.8610 |
| exposure | 0.6149 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
