# EMA Hourly Continuation — UNI/USDT P21_50

**Symbol:** UNI/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 435 |
| net_profit_factor | 0.6811 |
| net_win_rate | 0.4713 |
| gross_profit_factor | 0.8974 |
| gross_win_rate | 0.4713 |
| sharpe_ratio | -2.5574 |
| sortino_ratio | -0.7613 |
| max_drawdown | 0.5912 |
| cagr | -0.2945 |
| net_avg_win | 60.8096 |
| net_avg_loss | -79.5734 |
| avg_hold_time_bars | 7.1885 |
| exposure | 0.1421 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
