# EMA Hourly Continuation — PYTH/USDT P20_200

**Symbol:** PYTH/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 318 |
| net_profit_factor | 0.8645 |
| net_win_rate | 0.5252 |
| gross_profit_factor | 1.0996 |
| gross_win_rate | 0.5252 |
| sharpe_ratio | -0.7792 |
| sortino_ratio | -0.1995 |
| max_drawdown | 0.2987 |
| cagr | -0.0902 |
| net_avg_win | 80.7589 |
| net_avg_loss | -103.3125 |
| avg_hold_time_bars | 47.4151 |
| exposure | 0.6854 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
