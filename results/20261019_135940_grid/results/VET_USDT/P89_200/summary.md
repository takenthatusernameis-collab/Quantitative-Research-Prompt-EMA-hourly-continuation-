# EMA Hourly Continuation — VET/USDT P89_200

**Symbol:** VET/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 367 |
| net_profit_factor | 0.5951 |
| net_win_rate | 0.4768 |
| gross_profit_factor | 0.9859 |
| gross_win_rate | 0.4959 |
| sharpe_ratio | -3.1160 |
| sortino_ratio | -0.8427 |
| max_drawdown | 0.6463 |
| cagr | -0.3319 |
| net_avg_win | 53.4873 |
| net_avg_loss | -81.9184 |
| avg_hold_time_bars | 12.6757 |
| exposure | 0.2115 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
