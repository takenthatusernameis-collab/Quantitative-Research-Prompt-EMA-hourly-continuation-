# EMA Hourly Continuation — COTI/USDT P21_26

**Symbol:** COTI/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 152 |
| net_profit_factor | 0.8039 |
| net_win_rate | 0.5197 |
| gross_profit_factor | 1.0855 |
| gross_win_rate | 0.5197 |
| sharpe_ratio | -0.8573 |
| sortino_ratio | -0.1523 |
| max_drawdown | 0.2411 |
| cagr | -0.0678 |
| net_avg_win | 83.8909 |
| net_avg_loss | -112.9284 |
| avg_hold_time_bars | 4.9605 |
| exposure | 0.0343 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
