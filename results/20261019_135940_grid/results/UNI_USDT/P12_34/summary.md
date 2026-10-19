# EMA Hourly Continuation — UNI/USDT P12_34

**Symbol:** UNI/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1328 |
| net_profit_factor | 0.4438 |
| net_win_rate | 0.4337 |
| gross_profit_factor | 0.8775 |
| gross_win_rate | 0.4473 |
| sharpe_ratio | -9.9078 |
| sortino_ratio | -5.0639 |
| max_drawdown | 0.9984 |
| cagr | -0.9226 |
| net_avg_win | 13.8329 |
| net_avg_loss | -23.8718 |
| avg_hold_time_bars | 3.5602 |
| exposure | 0.2149 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
