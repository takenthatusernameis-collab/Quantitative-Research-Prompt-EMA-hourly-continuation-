# EMA Hourly Continuation — RAY/USDT P26_100

**Symbol:** RAY/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 671 |
| net_profit_factor | 0.6415 |
| net_win_rate | 0.4814 |
| gross_profit_factor | 0.9345 |
| gross_win_rate | 0.4918 |
| sharpe_ratio | -3.5941 |
| sortino_ratio | -1.3099 |
| max_drawdown | 0.8165 |
| cagr | -0.4674 |
| net_avg_win | 44.0103 |
| net_avg_loss | -63.6781 |
| avg_hold_time_bars | 10.0194 |
| exposure | 0.3056 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
