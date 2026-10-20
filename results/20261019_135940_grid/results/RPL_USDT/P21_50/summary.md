# EMA Hourly Continuation — RPL/USDT P21_50

**Symbol:** RPL/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 912 |
| net_profit_factor | 0.5346 |
| net_win_rate | 0.4507 |
| gross_profit_factor | 0.9404 |
| gross_win_rate | 0.4649 |
| sharpe_ratio | -6.4425 |
| sortino_ratio | -2.7352 |
| max_drawdown | 0.9654 |
| cagr | -0.7337 |
| net_avg_win | 26.9559 |
| net_avg_loss | -41.3646 |
| avg_hold_time_bars | 5.9232 |
| exposure | 0.2445 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
