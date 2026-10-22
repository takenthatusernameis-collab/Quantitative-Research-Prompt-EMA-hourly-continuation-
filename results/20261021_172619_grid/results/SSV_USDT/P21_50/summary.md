# EMA Hourly Continuation — SSV/USDT P21_50

**Symbol:** SSV/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 561 |
| net_profit_factor | 0.7250 |
| net_win_rate | 0.4813 |
| gross_profit_factor | 0.9529 |
| gross_win_rate | 0.4831 |
| sharpe_ratio | -2.6342 |
| sortino_ratio | -0.8895 |
| max_drawdown | 0.6559 |
| cagr | -0.3352 |
| net_avg_win | 62.7771 |
| net_avg_loss | -80.3418 |
| avg_hold_time_bars | 7.3832 |
| exposure | 0.1874 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
