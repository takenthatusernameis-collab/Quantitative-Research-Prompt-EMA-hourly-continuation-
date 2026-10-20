# EMA Hourly Continuation — DAG/USDT P12_20

**Symbol:** DAG/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1464 |
| net_profit_factor | 0.2998 |
| net_win_rate | 0.3163 |
| gross_profit_factor | 0.6660 |
| gross_win_rate | 0.3477 |
| sharpe_ratio | -16.9474 |
| sortino_ratio | -9.3444 |
| max_drawdown | 1.0000 |
| cagr | -0.9939 |
| net_avg_win | 9.2492 |
| net_avg_loss | -14.2681 |
| avg_hold_time_bars | 2.1311 |
| exposure | 0.1418 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
