# EMA Hourly Continuation — DGB/USDT P50_100

**Symbol:** DGB/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 757 |
| net_profit_factor | 0.4716 |
| net_win_rate | 0.4293 |
| gross_profit_factor | 0.8793 |
| gross_win_rate | 0.4425 |
| sharpe_ratio | -7.1392 |
| sortino_ratio | -2.7683 |
| max_drawdown | 0.9684 |
| cagr | -0.7474 |
| net_avg_win | 26.5958 |
| net_avg_loss | -42.4253 |
| avg_hold_time_bars | 5.2008 |
| exposure | 0.1790 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
