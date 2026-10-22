# EMA Hourly Continuation — JST/USDT P20_55

**Symbol:** JST/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 818 |
| net_profit_factor | 0.2902 |
| net_win_rate | 0.4315 |
| gross_profit_factor | 1.0035 |
| gross_win_rate | 0.4976 |
| sharpe_ratio | -8.7351 |
| sortino_ratio | -3.5428 |
| max_drawdown | 0.9901 |
| cagr | -0.8374 |
| net_avg_win | 11.4658 |
| net_avg_loss | -29.9894 |
| avg_hold_time_bars | 6.4279 |
| exposure | 0.2379 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
