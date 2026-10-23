# EMA Hourly Continuation — ETN/USDT P26_200

**Symbol:** ETN/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 504 |
| net_profit_factor | 0.4567 |
| net_win_rate | 0.3829 |
| gross_profit_factor | 0.6323 |
| gross_win_rate | 0.3869 |
| sharpe_ratio | -6.3885 |
| sortino_ratio | -2.1864 |
| max_drawdown | 0.8953 |
| cagr | -0.6566 |
| net_avg_win | 38.9455 |
| net_avg_loss | -52.9213 |
| avg_hold_time_bars | 17.4663 |
| exposure | 0.4782 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
