# EMA Hourly Continuation — AR/USDT P34_200

**Symbol:** AR/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 365 |
| net_profit_factor | 0.6070 |
| net_win_rate | 0.4438 |
| gross_profit_factor | 0.8243 |
| gross_win_rate | 0.4548 |
| sharpe_ratio | -3.0375 |
| sortino_ratio | -0.8114 |
| max_drawdown | 0.6431 |
| cagr | -0.3240 |
| net_avg_win | 59.6678 |
| net_avg_loss | -78.4501 |
| avg_hold_time_bars | 31.8822 |
| exposure | 0.5290 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
