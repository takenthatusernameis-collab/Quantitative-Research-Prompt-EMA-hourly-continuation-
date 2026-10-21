# EMA Hourly Continuation — AKT/USDT P12_50

**Symbol:** AKT/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 617 |
| net_profit_factor | 0.6957 |
| net_win_rate | 0.4700 |
| gross_profit_factor | 0.8632 |
| gross_win_rate | 0.4700 |
| sharpe_ratio | -2.6427 |
| sortino_ratio | -0.9345 |
| max_drawdown | 0.6751 |
| cagr | -0.3492 |
| net_avg_win | 52.0325 |
| net_avg_loss | -66.3286 |
| avg_hold_time_bars | 10.0357 |
| exposure | 0.2815 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
