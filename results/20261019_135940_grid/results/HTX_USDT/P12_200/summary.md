# EMA Hourly Continuation — HTX/USDT P12_200

**Symbol:** HTX/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 388 |
| net_profit_factor | 0.3583 |
| net_win_rate | 0.3789 |
| gross_profit_factor | 0.8400 |
| gross_win_rate | 0.4175 |
| sharpe_ratio | -7.1177 |
| sortino_ratio | -1.9839 |
| max_drawdown | 0.9418 |
| cagr | -0.6728 |
| net_avg_win | 35.7163 |
| net_avg_loss | -60.8005 |
| avg_hold_time_bars | 43.5387 |
| exposure | 0.7645 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
