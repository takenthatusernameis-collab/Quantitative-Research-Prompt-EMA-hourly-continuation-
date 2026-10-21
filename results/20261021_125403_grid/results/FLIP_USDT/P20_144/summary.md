# EMA Hourly Continuation — FLIP/USDT P20_144

**Symbol:** FLIP/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 341 |
| net_profit_factor | 0.6969 |
| net_win_rate | 0.4721 |
| gross_profit_factor | 0.8999 |
| gross_win_rate | 0.4751 |
| sharpe_ratio | -2.0985 |
| sortino_ratio | -0.5463 |
| max_drawdown | 0.4867 |
| cagr | -0.2253 |
| net_avg_win | 67.5734 |
| net_avg_loss | -86.7294 |
| avg_hold_time_bars | 34.5836 |
| exposure | 0.5360 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
