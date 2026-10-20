# EMA Hourly Continuation — EDU/USDT P21_34

**Symbol:** EDU/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1161 |
| net_profit_factor | 0.3808 |
| net_win_rate | 0.4177 |
| gross_profit_factor | 0.7453 |
| gross_win_rate | 0.4393 |
| sharpe_ratio | -9.5907 |
| sortino_ratio | -4.6301 |
| max_drawdown | 0.9968 |
| cagr | -0.8961 |
| net_avg_win | 12.6357 |
| net_avg_loss | -23.8095 |
| avg_hold_time_bars | 3.0482 |
| exposure | 0.1601 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
