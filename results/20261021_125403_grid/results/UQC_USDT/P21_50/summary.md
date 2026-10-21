# EMA Hourly Continuation — UQC/USDT P21_50

**Symbol:** UQC/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 260 |
| net_profit_factor | 0.4174 |
| net_win_rate | 0.3462 |
| gross_profit_factor | 0.6352 |
| gross_win_rate | 0.3538 |
| sharpe_ratio | -4.8693 |
| sortino_ratio | -1.0994 |
| max_drawdown | 0.7399 |
| cagr | -0.4114 |
| net_avg_win | 58.7003 |
| net_avg_loss | -74.4454 |
| avg_hold_time_bars | 42.9962 |
| exposure | 0.5060 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
