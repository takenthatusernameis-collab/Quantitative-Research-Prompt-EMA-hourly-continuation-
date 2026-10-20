# EMA Hourly Continuation — SQD/USDT P21_50

**Symbol:** SQD/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 916 |
| net_profit_factor | 0.6666 |
| net_win_rate | 0.4771 |
| gross_profit_factor | 1.0178 |
| gross_win_rate | 0.4847 |
| sharpe_ratio | -4.8491 |
| sortino_ratio | -2.1010 |
| max_drawdown | 0.9184 |
| cagr | -0.6335 |
| net_avg_win | 41.7614 |
| net_avg_loss | -57.1525 |
| avg_hold_time_bars | 4.9836 |
| exposure | 0.2146 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
