# EMA Hourly Continuation — LPT/USDT P8_50

**Symbol:** LPT/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1114 |
| net_profit_factor | 0.5268 |
| net_win_rate | 0.4336 |
| gross_profit_factor | 0.8087 |
| gross_win_rate | 0.4461 |
| sharpe_ratio | -7.2702 |
| sortino_ratio | -3.4068 |
| max_drawdown | 0.9851 |
| cagr | -0.8091 |
| net_avg_win | 22.6922 |
| net_avg_loss | -32.9699 |
| avg_hold_time_bars | 9.2190 |
| exposure | 0.4668 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
