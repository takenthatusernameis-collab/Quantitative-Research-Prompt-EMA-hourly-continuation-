# EMA Hourly Continuation — PYTH/USDT P26_200

**Symbol:** PYTH/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 259 |
| net_profit_factor | 0.9752 |
| net_win_rate | 0.5290 |
| gross_profit_factor | 1.1137 |
| gross_win_rate | 0.5290 |
| sharpe_ratio | -0.0847 |
| sortino_ratio | -0.0197 |
| max_drawdown | 0.1551 |
| cagr | -0.0137 |
| net_avg_win | 97.6349 |
| net_avg_loss | -112.4233 |
| avg_hold_time_bars | 50.9575 |
| exposure | 0.5999 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
