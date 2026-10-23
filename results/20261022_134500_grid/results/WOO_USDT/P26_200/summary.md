# EMA Hourly Continuation — WOO/USDT P26_200

**Symbol:** WOO/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 333 |
| net_profit_factor | 0.8170 |
| net_win_rate | 0.5105 |
| gross_profit_factor | 1.0901 |
| gross_win_rate | 0.5195 |
| sharpe_ratio | -1.3482 |
| sortino_ratio | -0.3454 |
| max_drawdown | 0.4846 |
| cagr | -0.1542 |
| net_avg_win | 90.1752 |
| net_avg_loss | -115.1087 |
| avg_hold_time_bars | 39.9700 |
| exposure | 0.6050 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
