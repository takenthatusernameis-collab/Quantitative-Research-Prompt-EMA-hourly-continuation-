# EMA Hourly Continuation — HNT/USDT P12_89

**Symbol:** HNT/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 542 |
| net_profit_factor | 0.7690 |
| net_win_rate | 0.4871 |
| gross_profit_factor | 0.9245 |
| gross_win_rate | 0.4871 |
| sharpe_ratio | -1.7551 |
| sortino_ratio | -0.5831 |
| max_drawdown | 0.5065 |
| cagr | -0.2370 |
| net_avg_win | 62.1581 |
| net_avg_loss | -76.7610 |
| avg_hold_time_bars | 19.7103 |
| exposure | 0.4856 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
