# EMA Hourly Continuation — SQD/USDT P21_55

**Symbol:** SQD/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 887 |
| net_profit_factor | 0.6615 |
| net_win_rate | 0.4814 |
| gross_profit_factor | 0.9930 |
| gross_win_rate | 0.4882 |
| sharpe_ratio | -4.5106 |
| sortino_ratio | -1.9141 |
| max_drawdown | 0.8963 |
| cagr | -0.6042 |
| net_avg_win | 40.9538 |
| net_avg_loss | -57.4650 |
| avg_hold_time_bars | 5.5423 |
| exposure | 0.2311 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
