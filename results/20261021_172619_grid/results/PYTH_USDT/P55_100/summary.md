# EMA Hourly Continuation — PYTH/USDT P55_100

**Symbol:** PYTH/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 327 |
| net_profit_factor | 0.7030 |
| net_win_rate | 0.4771 |
| gross_profit_factor | 0.8907 |
| gross_win_rate | 0.4771 |
| sharpe_ratio | -1.8778 |
| sortino_ratio | -0.4846 |
| max_drawdown | 0.4393 |
| cagr | -0.1997 |
| net_avg_win | 64.9975 |
| net_avg_loss | -84.3475 |
| avg_hold_time_bars | 8.3486 |
| exposure | 0.1241 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
