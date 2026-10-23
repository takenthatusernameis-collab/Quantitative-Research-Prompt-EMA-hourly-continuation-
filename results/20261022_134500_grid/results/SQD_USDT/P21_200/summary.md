# EMA Hourly Continuation — SQD/USDT P21_200

**Symbol:** SQD/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 450 |
| net_profit_factor | 0.7585 |
| net_win_rate | 0.4978 |
| gross_profit_factor | 0.9791 |
| gross_win_rate | 0.4978 |
| sharpe_ratio | -1.8390 |
| sortino_ratio | -0.5591 |
| max_drawdown | 0.5262 |
| cagr | -0.2332 |
| net_avg_win | 66.6433 |
| net_avg_loss | -87.0829 |
| avg_hold_time_bars | 26.9200 |
| exposure | 0.5694 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
