# EMA Hourly Continuation — NOT/USDT P89_200

**Symbol:** NOT/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 261 |
| net_profit_factor | 0.8414 |
| net_win_rate | 0.5134 |
| gross_profit_factor | 1.0311 |
| gross_win_rate | 0.5134 |
| sharpe_ratio | -0.8145 |
| sortino_ratio | -0.1919 |
| max_drawdown | 0.2079 |
| cagr | -0.0860 |
| net_avg_win | 77.6952 |
| net_avg_loss | -97.4288 |
| avg_hold_time_bars | 13.8736 |
| exposure | 0.1701 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
