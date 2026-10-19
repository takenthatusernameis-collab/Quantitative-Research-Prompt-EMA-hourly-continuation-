# EMA Hourly Continuation — RAY/USDT P55_100

**Symbol:** RAY/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 617 |
| net_profit_factor | 0.5132 |
| net_win_rate | 0.4587 |
| gross_profit_factor | 0.8295 |
| gross_win_rate | 0.4668 |
| sharpe_ratio | -5.0143 |
| sortino_ratio | -1.7668 |
| max_drawdown | 0.8903 |
| cagr | -0.5682 |
| net_avg_win | 32.7287 |
| net_avg_loss | -54.0378 |
| avg_hold_time_bars | 5.0340 |
| exposure | 0.1412 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
