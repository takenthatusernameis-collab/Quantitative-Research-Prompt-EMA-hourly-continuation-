# EMA Hourly Continuation — WOO/USDT P21_100

**Symbol:** WOO/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 460 |
| net_profit_factor | 0.7996 |
| net_win_rate | 0.4870 |
| gross_profit_factor | 0.9775 |
| gross_win_rate | 0.4870 |
| sharpe_ratio | -1.7663 |
| sortino_ratio | -0.5407 |
| max_drawdown | 0.5528 |
| cagr | -0.2216 |
| net_avg_win | 83.1509 |
| net_avg_loss | -98.7073 |
| avg_hold_time_bars | 20.0783 |
| exposure | 0.4198 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
