# EMA Hourly Continuation — GMT/USDT P20_55

**Symbol:** GMT/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 964 |
| net_profit_factor | 0.5358 |
| net_win_rate | 0.4440 |
| gross_profit_factor | 0.9100 |
| gross_win_rate | 0.4523 |
| sharpe_ratio | -7.1145 |
| sortino_ratio | -3.1279 |
| max_drawdown | 0.9784 |
| cagr | -0.7774 |
| net_avg_win | 26.3496 |
| net_avg_loss | -39.2682 |
| avg_hold_time_bars | 5.4191 |
| exposure | 0.2375 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
