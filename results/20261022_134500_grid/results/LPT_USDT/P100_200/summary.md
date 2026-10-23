# EMA Hourly Continuation — LPT/USDT P100_200

**Symbol:** LPT/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 408 |
| net_profit_factor | 0.5657 |
| net_win_rate | 0.4608 |
| gross_profit_factor | 0.8997 |
| gross_win_rate | 0.4755 |
| sharpe_ratio | -3.6820 |
| sortino_ratio | -1.0416 |
| max_drawdown | 0.7288 |
| cagr | -0.3971 |
| net_avg_win | 49.8495 |
| net_avg_loss | -75.2977 |
| avg_hold_time_bars | 9.5098 |
| exposure | 0.1764 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
