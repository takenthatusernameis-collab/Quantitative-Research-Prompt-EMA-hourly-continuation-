# EMA Hourly Continuation — HNT/USDT P26_100

**Symbol:** HNT/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 684 |
| net_profit_factor | 0.5129 |
| net_win_rate | 0.4298 |
| gross_profit_factor | 0.7552 |
| gross_win_rate | 0.4342 |
| sharpe_ratio | -5.3380 |
| sortino_ratio | -1.9642 |
| max_drawdown | 0.9138 |
| cagr | -0.6120 |
| net_avg_win | 32.4918 |
| net_avg_loss | -47.7555 |
| avg_hold_time_bars | 11.7442 |
| exposure | 0.3651 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
