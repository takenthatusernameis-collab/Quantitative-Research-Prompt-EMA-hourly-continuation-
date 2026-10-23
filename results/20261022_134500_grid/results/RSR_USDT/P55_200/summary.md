# EMA Hourly Continuation — RSR/USDT P55_200

**Symbol:** RSR/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 380 |
| net_profit_factor | 0.6997 |
| net_win_rate | 0.4816 |
| gross_profit_factor | 0.9456 |
| gross_win_rate | 0.4895 |
| sharpe_ratio | -2.1690 |
| sortino_ratio | -0.5950 |
| max_drawdown | 0.5094 |
| cagr | -0.2469 |
| net_avg_win | 64.8695 |
| net_avg_loss | -86.1166 |
| avg_hold_time_bars | 20.6947 |
| exposure | 0.3575 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
