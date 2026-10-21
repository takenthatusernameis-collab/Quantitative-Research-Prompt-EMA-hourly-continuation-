# EMA Hourly Continuation — EDU/USDT P21_200

**Symbol:** EDU/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 359 |
| net_profit_factor | 0.8442 |
| net_win_rate | 0.4986 |
| gross_profit_factor | 0.9895 |
| gross_win_rate | 0.4986 |
| sharpe_ratio | -0.9894 |
| sortino_ratio | -0.2674 |
| max_drawdown | 0.3288 |
| cagr | -0.1183 |
| net_avg_win | 82.3726 |
| net_avg_loss | -97.0300 |
| avg_hold_time_bars | 38.1086 |
| exposure | 0.6191 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
